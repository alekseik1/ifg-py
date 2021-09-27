from __future__ import division

import os

import numpy as np
from fdint import fdk, ifd1h

from ifg.units_converter import SiAtomicConverter
from ifg.utils import dump_to_csv

THRESHOLD = 1e10


def _1d_call(func, array, *args, **kwargs):
    return func(array.reshape(-1), *args, **kwargs).reshape(array.shape)


def _fdk(array, k):
    return fdk(k, array)


def get_chemical_potential(vv, tt, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG chemical potential mu in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: `mu[i][j]` - chemical potential in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    to_inverse = np.sqrt(2) * np.pi ** 2 / (gbar * tt ** (1.5) * vv)
    mu_div_temperature = _1d_call(ifd1h, to_inverse)
    mu = mu_div_temperature * tt
    #    mu = np.multiply(temperature, mu_div_temperature.T).T
    return mu


def get_F_potential(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG Helmholtz potential F in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :param chemical_potential: Chemical potential in atomic units.
    :return: F[i][j] - Helmholtz free energy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    # y = chemical_potential/temperature
    y = chemical_potential / tt
    F = gbar / np.sqrt(2.0) / np.pi ** 2 * tt ** (2.5) * vv
    F *= y * _1d_call(_fdk, y, k=0.5) - 2.0 / 3.0 * _1d_call(_fdk, y, k=1.5)
    return F


def get_pressure(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG pressure P in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: P[i][j] - Pressure in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
    pressure = (
        gbar * np.sqrt(2) / (3 * np.pi ** 2) * tt ** (2.5) * _1d_call(_fdk, y, k=1.5)
    )
    return pressure


def get_energy(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG energy E in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: E[i][j] - Energy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
    energy = (
        gbar * vv / (np.sqrt(2) * np.pi ** 2) * tt ** 2.5 * _1d_call(_fdk, y, k=1.5)
    )
    return energy


def get_entropy(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG entropy S in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: S[i][j] - Entropy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
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


def get_heat_capacity_volume(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG heat capacity C_V in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_V[i][j] - C_V in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
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


def get_heat_capacity_pressure(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG heat capacity C_P in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_P[i][j] - C_P in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
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


def get_sound_speed_temperature(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG sound speed C_T in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_T[i][j] - C_T in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
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


def get_sound_speed_entropy(vv, tt, chemical_potential, gbar=2.0, *args, **kwargs):
    # type: (np.ndarray, np.ndarray, np.ndarray, float, list, dict) -> np.ndarray
    """Get IFG sound speed C_S in atomic units.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :param gbar: degeneracy factor, for IFG g = 2s + 1
    :return: C_S[i][j] - C_S in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = chemical_potential / tt
    C_S = (
        np.sqrt(5)
        * np.sqrt(gbar)
        * 2 ** (1 / 4)
        / (3 * np.pi)
        * tt ** (5 / 4)
        * np.sqrt(vv * _1d_call(_fdk, y, k=3 / 2))
    )
    return C_S


def get_all_properties(vv, tt, gbar=2.0, csv_dir=None):
    # type: (np.ndarray, np.ndarray, float, str) -> dict
    """Calculate all properties and save them to csv file.

    :param vv: Matrix of specific volumes in atomic units.
    :param tt: Matrix of temperatures in atomic units.
    :param vv: Specific volume in atomic units
    :param tt: Temperature in atomic units
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
            vv=vv, tt=tt, gbar=gbar, chemical_potential=properties["mu"]
        )
        if csv_dir:
            for i, volume in enumerate(vv[0, :]):
                dump_to_csv(
                    os.path.join(
                        os.getcwd(),
                        csv_dir,
                        "{}_v={}_atomic_units.csv".format(key, volume),
                    ),
                    np.array([tt[0, :], properties[key][:, i]]).T,
                )
    return properties


class IfgCalculator:
    def __init__(
        self,
        temperatures=None,
        volumes=None,
        thetas=None,
        densities=None,
        rs=None,
        input_in_si=None,
        output_in_si=None,
        g=None,
        mr=None,
    ):
        #    def __init__(self, specific_volumes, temperatures,
        #                 input_in_si, output_in_si, g=2., mr=1.):
        # type: (np.ndarray, np.ndarray, bool, bool, float, float) -> None
        """Main class for IFG calculations.

        :param volumes, rs, densities: Array of volumes, rs or densities, respectively
            (only one parameter is possible)
        :param temperatures, thetas: Array of temperatures or thetas, respectively
            (only one parameter is possible; in case of thetas the length of
            thetas array should be not more than 1)
        :param input_in_is: Whether input values are in SI units (False - atomic units, default)
        :param output_in_si: Whether output values are in SI units (False - atomic units, default)
        :param g: degeneracy of spin states, g = 2s + 1, s - spin, g = 2 by default
        :param mr: mass of particles with respect to electron mass, mr = 1 by default
        """
        # Default values
        input_in_si_default = False
        output_in_si_default = False
        g_default = 2.0
        mr_default = 1.0

        # Checking if temperatures or thetas argument is given
        if temperatures is None and thetas is None:
            raise ValueError("temperatures or thetas parameter is obligatory")
        # Checking if both temperatures and thetas arguments are given
        if temperatures is not None and thetas is not None:
            raise ValueError(
                "Only one named parameter must be used for temperature: temperatures or thetas"
            )

        # Checking if any of volumes or densities of rs argument is given
        if volumes is None and densities is None and rs is None:
            raise ValueError(
                "One of volumes or densities or rs parameter is obligatory"
            )

        # Cannot have more than one argument
        if sum([x is not None for x in (volumes, densities, rs)]) > 1:
            raise ValueError(
                "Only one named parameter must be used for volume: volumes or densities or rs"
            )

        # If volumes argument is given, simply convert to np.ndarray
        if volumes is not None:
            volumes = np.array(volumes)

        # If densities argument is given, calculate volumes
        if densities is not None:
            volumes = 1.0 / np.array(densities)

        # If rs argument is given, calculate volumes
        if rs is not None:
            volumes = 4.0 * np.pi * np.array(rs) ** 3 / 3.0

        # If temperatures argument is given, simply convert to np.ndarray
        if temperatures is not None:
            temperatures = np.array(temperatures)

        # thetas argument is a special case: theta depends both on temperature and volume
        # Calculate vv and tt matrices, for thetas using cycle, otherwise using np.meshgrid
        if thetas is not None:
            thetas = np.array(thetas)
            tt = np.zeros((len(thetas), len(volumes)))
            vv = np.zeros((len(thetas), len(volumes)))
            i = 0
            for th in thetas:
                j = 0
                for v in volumes:
                    tt[i, j] = 0.5 * th * (3.0 * np.pi * np.pi / v) ** (2.0 / 3.0)
                    vv[i, j] = v
                    j = j + 1
                i = i + 1
        else:
            vv, tt = np.meshgrid(volumes, temperatures)

        if input_in_si is not None:
            self.input_in_si = input_in_si
        else:
            self.input_in_si = input_in_si_default

        if output_in_si is not None:
            self.output_in_si = output_in_si
        else:
            self.output_in_si = output_in_si_default

        self.g = g if g is not None else g_default
        self.mr = mr if mr is not None else mr_default

        self.gbar = self.g * self.mr ** 1.5
        self.converter = SiAtomicConverter(from_si=True)
        self.reverse_converter = SiAtomicConverter(from_si=False)
        vv, tt = map(np.array, [vv, tt])
        self.vv = self.converter.convert_volume(vv) if self.input_in_si else vv
        self.tt = self.converter.convert_temperature(tt) if self.input_in_si else tt

    def generic_getter(self, calc_function, attribute_name, convert_function):
        cache = "__{}_cached__".format(attribute_name)
        if hasattr(self, cache):
            # return cached value if possible
            return getattr(self, cache)
        elif attribute_name == "mu":
            # `mu` is a special case since it is used in `calc_function` below
            return get_chemical_potential(vv=self.vv, tt=self.tt, gbar=self.gbar)
        # Cache is not available
        value = calc_function(
            vv=self.vv, tt=self.tt, chemical_potential=self.mu, gbar=self.gbar
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
                for i, volume in enumerate(self.vv[0, :]):
                    dump_to_csv(
                        os.path.join(
                            os.getcwd(),
                            csv_dir,
                            "{}_v={}_atomic_units.csv".format(key, volume),
                        ),
                        np.array([self.tt[0, :], value[:, i]]).T,
                    )
        return properties
