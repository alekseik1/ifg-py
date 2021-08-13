from __future__ import division

import os
from typing import Iterable

import numpy as np
from fdint import fdk, ifd1h

from ifg.units_converter import SiAtomicConverter, convert_r_s_to_specific_volume
from ifg.utils import dump_to_csv

THRESHOLD = 1e10


def _1d_call(func, array, *args, **kwargs):
    return func(array.reshape(-1), *args, **kwargs).reshape(array.shape)


def _fdk(array, k):
    return fdk(k, array)


def get_chemical_potential(specific_volume, temperature, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG chemical potential mu in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: `mu[i][j]` - chemical potential in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    vv, tt = np.meshgrid(specific_volume, temperature)
    to_inverse = np.sqrt(2) * np.pi ** 2 / (gbar * tt ** (1.5) * vv)
    mu_div_temperature = _1d_call(ifd1h, to_inverse)
    mu = np.multiply(temperature, mu_div_temperature.T).T
    return mu


def get_F_potential(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG Helmholtz potential F in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :param chemical_potential: Chemical potential in atomic units.
    :return: F[i][j] - Helmholtz free energy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    # y = chemical_potential/temperature
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    F = gbar / np.sqrt(2.0) / np.pi ** 2 * tt ** (2.5) * vv
    F *= y * _1d_call(_fdk, y, k=0.5) - 2.0 / 3.0 * _1d_call(_fdk, y, k=1.5)
    return F


def get_pressure(temperature, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG pressure P in atomic units.

    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: P[i][j] - Pressure in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    specific_volume = np.empty(1)
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    pressure = (
        gbar * np.sqrt(2) / (3 * np.pi ** 2) * tt ** (2.5) * _1d_call(_fdk, y, k=1.5)
    )
    return pressure


def get_energy(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG energy E in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: E[i][j] - Energy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    energy = (
        gbar * vv / (np.sqrt(2) * np.pi ** 2) * tt ** 2.5 * _1d_call(_fdk, y, k=1.5)
    )
    return energy


def get_entropy(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG entropy S in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: S[i][j] - Entropy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    # There is a precision problem with "-" (minus) operator
    # We'll use asymptotic formula for low temperatures to avoid that problem
    y_low = y[y < THRESHOLD]
    vv_low, vv_high = vv[y < THRESHOLD], vv[y >= THRESHOLD]
    tt_low, tt_high = tt[y < THRESHOLD], tt[y >= THRESHOLD]
    # high temperatures - low numbers
    S_low = (
        -gbar
        * np.sqrt(2)
        / (6 * np.pi ** 2)
        * tt_low ** (3 / 2)
        * vv_low
        * (
            3 * y_low * _1d_call(_fdk, y_low, k=1 / 2)
            - 5 * _1d_call(_fdk, y_low, k=3 / 2)
        )
    )
    # low temperatures - high numbers
    S_high = (gbar * np.pi / 6) ** (2 / 3) * tt_high * vv_high ** (2 / 3)
    return np.concatenate((S_low, S_high)).reshape(y.shape)


def get_heat_capacity_volume(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG heat capacity C_V in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_V[i][j] - C_V in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    # There is a precision problem with "-" (minus) operator
    # We'll use asymptotic formula for high temperatures to avoid that problem
    y_low = y[y < THRESHOLD]
    vv_low, vv_high = vv[y < THRESHOLD], vv[y >= THRESHOLD]
    tt_low, tt_high = tt[y < THRESHOLD], tt[y >= THRESHOLD]
    # high temperatures - low numbers
    C_V_low = 5 * _1d_call(_fdk, y_low, k=-1 / 2) * _1d_call(_fdk, y_low, k=3 / 2)
    C_V_low -= 9 * _1d_call(_fdk, y_low, k=1 / 2) ** 2
    C_V_low *= gbar * np.sqrt(2) / (4 * np.pi ** 2) * tt_low ** (3 / 2) * vv_low
    C_V_low /= _1d_call(_fdk, y_low, k=-1 / 2)
    # low temperatures - high numbers
    C_V_high = (gbar * np.pi / 6) ** (2 / 3) * tt_high * vv_high ** (2 / 3)
    return np.concatenate((C_V_low, C_V_high)).reshape(y.shape)


def get_heat_capacity_pressure(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG heat capacity C_P in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_P[i][j] - C_P in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    # There is a precision problem with "-" (minus) operator
    # We'll use asymptotic formula for high temperatures to avoid that problem
    y_low = y[y < THRESHOLD]
    vv_low, vv_high = vv[y < THRESHOLD], vv[y >= THRESHOLD]
    tt_low, tt_high = tt[y < THRESHOLD], tt[y >= THRESHOLD]
    # high temperatures - low numbers
    C_P_low = 5 * gbar * np.sqrt(2) / (36 * np.pi ** 2) * tt_low ** (3 / 2) * vv_low
    C_P_low *= (
        5 * _1d_call(_fdk, y_low, k=-1 / 2) * _1d_call(_fdk, y_low, k=3 / 2)
        - 9 * _1d_call(_fdk, y_low, k=1 / 2) ** 2
    )
    C_P_low *= _1d_call(_fdk, y_low, k=3 / 2) / _1d_call(_fdk, y_low, k=1 / 2) ** 2
    # low temperatures - high numbers
    C_P_high = (gbar * np.pi / 6) ** (2 / 3) * tt_high * vv_high ** (2 / 3)
    return np.concatenate((C_P_low, C_P_high)).reshape(y.shape)


def get_sound_speed_temperature(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG sound speed C_T in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_T[i][j] - C_T in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_T = (
        2 ** (1 / 4)
        * np.sqrt(gbar)
        / np.pi
        * np.sqrt(vv)
        * tt ** (5 / 4)
        * _1d_call(_fdk, y, k=1 / 2)
        / np.sqrt(_1d_call(_fdk, y, k=-1 / 2))
    )
    return C_T


def get_sound_speed_entropy(
    specific_volume, temperature, chemical_potential, gbar=2.0, *args, **kwargs
):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG sound speed C_S in atomic units.

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_S[i][j] - C_S in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_S = (
        np.sqrt(5)
        * np.sqrt(gbar)
        * 2 ** (1 / 4)
        / (3 * np.pi)
        * tt ** (5 / 4)
        * np.sqrt(vv * _1d_call(_fdk, y, k=3 / 2))
    )
    return C_S


def get_all_properties(specific_volume, temperature_range, gbar=2.0, csv_dir=None):
    # type: (np.ndarray, np.ndarray, float, str) -> dict
    """Calculate all properties and save them to csv file.

    :param specific_volume: Specific volume in atomic units
    :param temperature_range: Temperature in atomic units
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :param csv_dir: Directory to save csv files to
    :return: dict {'property_name': ndarray}
    """
    properties = dict(
        mu=get_chemical_potential,
        F=get_F_potential,
        p=get_pressure,
        S=get_entropy,
        C_P=get_heat_capacity_pressure,
        C_V=get_heat_capacity_volume,
        C_T=get_sound_speed_temperature,
        C_S=get_sound_speed_entropy,
    )
    for key in properties.keys():
        properties[key] = properties[key](
            specific_volume=specific_volume,
            temperature=temperature_range,
            gbar=gbar,
            chemical_potential=properties["mu"],
        )
        if csv_dir:
            for i, volume in enumerate(specific_volume):
                dump_to_csv(
                    os.path.join(
                        os.getcwd(),
                        csv_dir,
                        "{}_v={}_atomic_units.csv".format(key, volume),
                    ),
                    np.array([temperature_range, properties[key][:, i]]).T,
                )
    return properties


class IfgCalculator:
    """Main class for IFG calculations. Implementation uses atomic units.

    All gas parameters are set by `with_<parameter>` functions, e.g.

    >>> IfgCalculator().with_temperatures([1., 2.])

    Temeperature is set as an array (pythonic or NumPy) of floats,
    supports both SI and atomic systems.

    Volume is set as an array (pythonic or NumPy) of flaots,
    supports both SI and atomic systems. It can also be expressed in terms of r_s value:

    4/3 pi r_s^3 = 1/n,

    where n denotes concentration.

    Required paramters are temperature and volume. Minimal working example:

    >>> calculator = IfgCalculator().with_temperatures([1., 2.]).with_volumes([0.1, 0.2])
    >>> calculator.C_P  # calculate heat isobaric heat capacity
    >>> calculator.mu  # get chemical potential
    """

    _required_input = ["temperatures", "volumes"]
    temperatures = None
    volumes = None
    output_in_si = False

    def __init__(self):
        self.relative_mass = 1.0
        self.g = 2
        self.converter = SiAtomicConverter(from_si=True)
        self.reverse_converter = SiAtomicConverter(from_si=False)

    def with_temperatures(self, temperatures, in_si=False):
        # type: (Iterable, bool) -> IfgCalculator
        temperatures = np.array(temperatures)
        self.temperatures = (
            self.converter.convert_temperature(temperatures) if in_si else temperatures
        )
        return self

    def with_volumes(self, volumes, in_si=False):
        # type: (Iterable, bool) -> IfgCalculator
        volumes = np.array(volumes)
        self.volumes = self.converter.convert_volume(volumes) if in_si else volumes

        return self

    def with_r_s(self, r_s, in_si=False):
        # type: (Iterable, bool) -> IfgCalculator
        # 4/3 pi r_s ^ 3 = specific_volume
        volumes = convert_r_s_to_specific_volume(r_s)
        if in_si:
            self.volumes = self.converter.convert_volume(volumes)
        else:
            self.volumes = volumes
        return self

    @property
    def gbar(self):
        return self.g * self.relative_mass ** 1.5

    def with_degeneracy(self, g):
        # type: (float) -> IfgCalculator
        self.g = g
        return self

    def with_relative_mass(self, relative_mass):
        # type: (float) -> IfgCalculator
        self.relative_mass = relative_mass
        return self

    def with_output_in_si(self, output_in_si=True):
        # type: (bool) -> IfgCalculator
        self.output_in_si = output_in_si
        return self

    def generic_getter(self, calc_function, attribute_name, convert_function):
        # Check for required arguments
        for name in self._required_input:
            if getattr(self, name) is None:
                raise ValueError("{} is not set".format(name))
        cache = "__{}_cached__".format(attribute_name)
        if hasattr(self, cache):
            # return cached value if possible
            return getattr(self, cache)
        elif attribute_name == "mu":
            # `mu` is a special case since it is used in `calc_function` below
            return get_chemical_potential(
                specific_volume=self.volumes,
                temperature=self.temperatures,
                gbar=self.gbar,
            )
        # Cache is not available
        value = calc_function(
            specific_volume=self.volumes,
            temperature=self.temperatures,
            chemical_potential=self.mu,
            gbar=self.gbar,
        )
        if self.output_in_si:
            # Call `convert_function` on `value` if output is in SI
            value = getattr(self.reverse_converter, convert_function)(value)
        # Store cache
        setattr(self, cache, value)
        return value

    @property
    def mu(self):
        """Get IFG chemical potential mu in atomic units.

        :return: `mu[i][j]` - chemical potential in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(get_chemical_potential, "mu", "convert_energy")

    @property
    def F(self):
        """Get IFG Helmholtz potential F in atomic units.

        :return: F[i][j] - Helmholtz free energy in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(get_F_potential, "F", "convert_energy")

    @property
    def P(self):
        """Get IFG pressure P in atomic units.

        :return: P[i][j] - Pressure in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(get_pressure, "p", "convert_pressure")

    @property
    def E(self):
        """Get IFG energy E in atomic units.

        :return: E[i][j] - Energy in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(get_energy, "E", "convert_energy")

    @property
    def S(self):
        """Get IFG entropy S in atomic units.

        :return: S[i][j] - Entropy in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(get_entropy, "S", "convert_entropy")

    @property
    def C_V(self):
        """Get IFG heat capacity C_V in atomic units.

        :return: C_V[i][j] - C_V in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(
            get_heat_capacity_volume, "C_V", "convert_heat_capacity"
        )

    @property
    def C_P(self):
        """Get IFG heat capacity C_P in atomic units.

        :return: C_P[i][j] - C_P in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(
            get_heat_capacity_pressure, "C_P", "convert_heat_capacity"
        )

    @property
    def C_T(self):
        """Get IFG sound speed C_T in atomic units.

        :return: C_T[i][j] - C_T in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(
            get_sound_speed_temperature, "C_T", "convert_sound_speed"
        )

    @property
    def C_S(self):
        """Get IFG sound speed C_S in atomic units.

        :return: C_S[i][j] - C_S in atomic units.\
        *i*-th index is for temperature, *j*-th one is for volume
        """
        return self.generic_getter(
            get_sound_speed_entropy, "C_S", "convert_sound_speed"
        )

    def get_all_properties(self, csv_dir=None):
        # type: (str) -> dict
        """Calculate all properties and save them to csv file.

        :param csv_dir: Directory to save csv files to
        :return: dict {'property_name': ndarray}
        """
        properties = {
            prop: getattr(self, prop)
            for prop in ["mu", "F", "P", "E", "S", "C_P", "C_V", "C_T", "C_S"]
        }
        if csv_dir is not None:
            for key, value in properties.items():
                for i, volume in enumerate(self.volumes):
                    dump_to_csv(
                        os.path.join(
                            os.getcwd(),
                            csv_dir,
                            "{}_v={}_atomic_units.csv".format(key, volume),
                        ),
                        np.array([self.temperatures, value[:, i]]).T,
                    )
        return properties
