from ifg_py.utils import dump_to_csv
import os
from fdint import fdk, ifd1h
import numpy as np
from ifg_py.units_converter import SiAtomicConverter
from functools import wraps


def _1d_call(func, array, *args, **kwargs):
    return func(array.reshape(-1), *args, **kwargs).reshape(array.shape)


def _fdk(array, k):
    return fdk(k, array)


def get_chemical_potential(specific_volume: np.ndarray, temperature: np.ndarray,
                           *args, **kwargs) -> np.ndarray:
    """
    Get IFG chemical potential mu in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :return: `mu[i][j]` - chemical potential in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    g = 2
    vv, tt = np.meshgrid(specific_volume, temperature)
    to_inverse = np.sqrt(2) * np.pi ** 2 / (g * tt ** (3 / 2) * vv)
    mu_div_temperature = _1d_call(ifd1h, to_inverse)
    mu = np.multiply(temperature, mu_div_temperature.T).T
    return mu


def get_F_potential(specific_volume: np.ndarray, temperature: np.ndarray,
                    chemical_potential: np.ndarray,
                    *args, **kwargs) -> np.ndarray:
    """
    Get IFG Helmholtz potential F in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: F[i][j] - Helmholtz free energy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    # y = chemical_potential/temperature
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    F = np.sqrt(2) / np.pi ** 2 * tt ** (5 / 2) * vv
    F *= (y * _1d_call(_fdk, y, k=1 / 2) - 2 / 3 * _1d_call(_fdk, y, k=3 / 2))
    return F


def get_pressure(temperature: np.ndarray, chemical_potential: np.ndarray,
                 *args, **kwargs) -> np.ndarray:
    """
    Get IFG pressure P in atomic units

    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: P[i][j] - Pressure in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    specific_volume = np.empty(1)
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    pressure = 2 * np.sqrt(2) / (3 * np.pi ** 2) * \
        tt ** (5 / 2) * _1d_call(_fdk, y, k=3 / 2)
    return pressure


def get_entropy(specific_volume: np.ndarray, temperature: np.ndarray,
                chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG entropy S in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: S[i][j] - Entropy in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    S = -np.sqrt(2) / (3 * np.pi ** 2) * tt ** (3 / 2) * vv * \
        (3 * y * _1d_call(_fdk, y, k=1 / 2) - 5 * _1d_call(_fdk, y, k=3 / 2))
    return S


def get_heat_capacity_volume(specific_volume: np.ndarray,
                             temperature: np.ndarray,
                             chemical_potential: np.ndarray,
                             *args, **kwargs) -> np.ndarray:
    """
    Get IFG heat capacity C_V in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_V[i][j] - C_V in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_V = np.sqrt(2) / (2 * np.pi ** 2) * tt ** (3 / 2) * vv
    C_V *= (5 * _1d_call(_fdk, y, k=-1 / 2) * _1d_call(_fdk, y, k=3 / 2)
            - 9 * _1d_call(_fdk, y, k=1 / 2) ** 2)
    C_V /= _1d_call(_fdk, y, k=-1 / 2)
    return C_V


def get_heat_capacity_pressure(specific_volume: np.ndarray, temperature: np.ndarray,
                               chemical_potential: np.ndarray,
                               *args, **kwargs) -> np.ndarray:
    """
    Get IFG heat capacity C_P in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_P[i][j] - C_P in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_P = 5 * np.sqrt(2) / (18 * np.pi ** 2) * tt ** (3 / 2) * vv
    C_P *= (5 * _1d_call(_fdk, y, k=-1 / 2) * _1d_call(_fdk, y, k=3 / 2)
            - 9 * _1d_call(_fdk, y, k=1 / 2) ** 2)
    C_P *= _1d_call(_fdk, y, k=3 / 2) / _1d_call(_fdk, y, k=1 / 2) ** 2
    return C_P


def get_sound_speed_temperature(specific_volume: np.ndarray, temperature: np.ndarray,
                                chemical_potential: np.ndarray,
                                *args, **kwargs) -> np.ndarray:
    """
    Get IFG sound speed C_T in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_T[i][j] - C_T in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_T = 2 ** (3 / 4) / np.pi * np.sqrt(vv) * tt ** (5 / 4) * \
        _1d_call(_fdk, y, k=1 / 2) / np.sqrt(_1d_call(_fdk, y, k=-1 / 2))
    return C_T


def get_sound_speed_entropy(specific_volume: np.ndarray, temperature: np.ndarray,
                            chemical_potential: np.ndarray,
                            *args, **kwargs) -> np.ndarray:
    """
    Get IFG sound speed C_S in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_S[i][j] - C_S in atomic units.
    *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1 / temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_S = np.sqrt(10) * 2 ** (1 / 4) / (3 * np.pi) * tt ** (5 / 4) * \
        np.sqrt(vv * _1d_call(_fdk, y, k=3 / 2))
    return C_S


def get_all_properties(specific_volume: np.ndarray,
                       temperature_range: np.ndarray,
                       csv_dir: str = None):
    """
    Calculate all properties and save them to csv file

    :param specific_volume: Specific volume in atomic units
    :param temperature_range: Temperature in atomic units
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
        C_S=get_sound_speed_entropy
    )
    for key in properties.keys():
        properties[key] = properties[key](specific_volume=specific_volume,
                                          temperature=temperature_range,
                                          chemical_potential=properties['mu'])
        if csv_dir:
            for i, volume in enumerate(specific_volume):
                dump_to_csv(
                    os.path.join(os.getcwd(), csv_dir,
                                 f'{key}_v={volume}_atomic_units.csv'),
                    np.array([temperature_range, properties[key][:, i]]).T)
    return properties


def ensure_mu(fn):
    @wraps(fn)
    def wrapped(self, *args, **kwargs):
        if self.chemical_potential is None:
            self.chemical_potential = get_chemical_potential(
                self.volumes, self.temperatures)
        return fn(self, *args, **kwargs)

    return wrapped


class IfgCalculator:

    def __init__(self, specific_volumes: np.ndarray, temperatures: np.ndarray,
                 input_in_si: bool, output_in_si: bool):
        """
        Main class for IFG calculations

        :param specific_volumes: Array of specific volumes of a gas
        :param temperatures: Array of temperatures of a gas
        :param input_in_si: Whether values are in SI or in atomic units
        """
        self.input_in_si = input_in_si
        self.output_in_si = output_in_si
        self.converter = SiAtomicConverter(from_si=True)
        self.reverse_converter = SiAtomicConverter(from_si=False)
        self.volumes = self.converter.convert_volume(specific_volumes) \
            if input_in_si else specific_volumes
        self.temperatures = self.converter.convert_temperature(temperatures) \
            if input_in_si else temperatures
        self.chemical_potential = None

    @ensure_mu
    def get_chemical_potential(self):
        """
        Get IFG chemical potential mu in atomic units

        :return: `mu[i][j]` - chemical potential in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        if self.output_in_si:
            return self.converter.convert_energy(self.chemical_potential)
        return self.chemical_potential

    @ensure_mu
    def get_F_potential(self):
        """
        Get IFG Helmholtz potential F in atomic units

        :return: F[i][j] - Helmholtz free energy in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.F_potential = get_F_potential(
            specific_volume=self.volumes, temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_energy(self.F_potential)
        return self.F_potential

    @ensure_mu
    def get_pressure(self):
        """
        Get IFG pressure P in atomic units

        :return: P[i][j] - Pressure in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.pressure = get_pressure(
            temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_pressure(self.pressure)
        return self.pressure

    @ensure_mu
    def get_entropy(self):
        """
        Get IFG entropy S in atomic units

        :return: S[i][j] - Entropy in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.entropy = get_entropy(
            specific_volume=self.volumes, temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_entropy(self.entropy)
        return self.entropy

    @ensure_mu
    def get_heat_capacity_volume(self):
        """
        Get IFG heat capacity C_V in atomic units

        :return: C_V[i][j] - C_V in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.heat_capacity_volume = get_heat_capacity_volume(
            specific_volume=self.volumes, temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_heat_capacity(
                self.heat_capacity_volume)
        return self.heat_capacity_volume

    @ensure_mu
    def get_heat_capacity_pressure(self):
        """
        Get IFG heat capacity C_P in atomic units

        :return: C_P[i][j] - C_P in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.heat_capacity_pressure = get_heat_capacity_pressure(
            specific_volume=self.volumes, temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_heat_capacity(
                self.heat_capacity_pressure)
        return self.heat_capacity_pressure

    @ensure_mu
    def get_sound_speed_temperature(self):
        """
        Get IFG sound speed C_T in atomic units

        :return: C_T[i][j] - C_T in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.sound_speed_temperature = get_sound_speed_temperature(
            specific_volume=self.volumes, temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_sound_speed(
                self.sound_speed_temperature)
        return self.sound_speed_temperature

    @ensure_mu
    def get_sound_speed_entropy(self):
        """
        Get IFG sound speed C_S in atomic units

        :return: C_S[i][j] - C_S in atomic units.
        *i*-th index is for temperature, *j*-th one is for volume
        """
        self.sound_speed_entropy = get_sound_speed_entropy(
            specific_volume=self.volumes, temperature=self.temperatures,
            chemical_potential=self.chemical_potential)
        if self.output_in_si:
            return self.converter.convert_sound_speed(
                self.sound_speed_temperature)
        return self.sound_speed_temperature

    def get_all_properties(self, csv_dir: str = None):
        """
        Calculate all properties and save them to csv file

        :param csv_dir: Directory to save csv files to
        :return: dict {'property_name': ndarray}
        """
        properties = dict(
            mu=self.get_chemical_potential,
            F=self.get_F_potential,
            p=self.get_pressure,
            S=self.get_entropy,
            C_P=self.get_heat_capacity_pressure,
            C_V=self.get_heat_capacity_volume,
            C_T=self.get_sound_speed_temperature,
            C_S=self.get_sound_speed_entropy
        )
        for key in properties.keys():
            properties[key] = properties[key]()
            if csv_dir:
                for i, volume in enumerate(self.volumes):
                    dump_to_csv(
                        os.path.join(os.getcwd(), csv_dir,
                                     f'{key}_v={volume}_atomic_units.csv'),
                        np.array([self.temperatures, properties[key][:, i]]).T)
        return properties
