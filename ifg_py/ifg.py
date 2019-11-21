from ifg_py.utils import dump_to_csv
import os
from fdint import fdk, ifd1h
import numpy as np


def _1d_call(func, array, *args, **kwargs):
    return func(array.reshape(-1), *args, **kwargs).reshape(array.shape)


def _fdk(array, k, *args, **kwargs):
    return fdk(k, array, *args, **kwargs)


def get_chemical_potential(specific_volume: np.ndarray, temperature: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG chemical potential mu in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :return: `mu[i][j]` - chemical potential in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    g = 2
    gamma_32 = np.sqrt(np.pi)/2
    vv, tt = np.meshgrid(specific_volume, temperature)
    # TODO: опять подгоны. Не нужно делить на Г(3/2), у меня нет объяснений
    #to_inverse = np.sqrt(2)*np.pi**2 / (g * temperature ** (3 / 2) * specific_volume * gamma_32)
    to_inverse = np.sqrt(2)*np.pi**2 / (g * tt ** (3 / 2) * vv)
    mu_T = _1d_call(ifd1h, to_inverse)
    # Multiply mu/T and corresponding T (same T[i] for same specific volumes)
    # Test it with: `np.all([mu[i] - mu_T[i]*temperature[i] == 0 for i in range(len(mu))])`
    mu = np.multiply(temperature, mu_T.T).T
    return mu


def get_F_potential(specific_volume: np.ndarray, temperature: np.ndarray,
                    chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG Helmholtz potential F in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: F[i][j] - Helmholtz free energy in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    # y = chemical_potential/temperature
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    # tested with: `np.sum([y[i] - chemical_potential[i]/temperature[i] for i in range(len(temperature))])`
    # gives e-12 error (due to division)
    F = np.sqrt(2)/np.pi**2 * tt**(5/2)*vv
    F *= (y * _1d_call(_fdk, y, k=1 / 2) - 2/3 * _1d_call(_fdk, y, k=3/2))
    return F


def get_pressure(temperature: np.ndarray, chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG pressure P in atomic units

    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: P[i][j] - Pressure in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    specific_volume = np.empty(1)
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    pressure = 2*np.sqrt(2)/(3*np.pi**2) * tt**(5/2)*_1d_call(_fdk, y, k=3/2)
    return pressure


def get_entropy(specific_volume: np.ndarray, temperature: np.ndarray,
                chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG entropy S in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: S[i][j] - Entropy in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    S = -np.sqrt(2)/(3*np.pi**2) * tt**(3/2)*vv*(3*y*_1d_call(_fdk, y, k=1/2) - 5*_1d_call(_fdk, y, k=3/2))
    return S


def get_heat_capacity_volume(specific_volume: np.ndarray, temperature: np.ndarray,
                             chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG heat capacity C_V in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_V[i][j] - C_V in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_V = np.sqrt(2)/(2*np.pi**2) * tt**(3/2)*vv
    C_V *= (5*_1d_call(_fdk, y, k=-1/2)*_1d_call(_fdk, y, k=3/2) - 9*_1d_call(_fdk, y, k=1/2)**2)
    C_V /= _1d_call(_fdk, y, k=-1/2)
    return C_V


def get_heat_capacity_pressure(specific_volume: np.ndarray, temperature: np.ndarray,
                               chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG heat capacity C_P in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_P[i][j] - C_P in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_P = 5*np.sqrt(2)/(18*np.pi**2) * tt**(3/2)*vv
    C_P *= (5*_1d_call(_fdk, y, k=-1/2)*_1d_call(_fdk, y, k=3/2) - 9*_1d_call(_fdk, y, k=1/2)**2)
    C_P *= _1d_call(_fdk, y, k=3/2)/_1d_call(_fdk, y, k=1/2)**2
    return C_P


def get_sound_speed_temperature(specific_volume: np.ndarray, temperature: np.ndarray,
                                chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG sound speed C_T in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_T[i][j] - C_T in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_T = 2**(3/4)/np.pi * np.sqrt(vv)*tt**(5/4)*_1d_call(_fdk, y, k=1/2)/np.sqrt(_1d_call(_fdk, y, k=-1/2))
    return C_T


def get_sound_speed_entropy(specific_volume: np.ndarray, temperature: np.ndarray,
                            chemical_potential: np.ndarray, *args, **kwargs) -> np.ndarray:
    """
    Get IFG sound speed C_S in atomic units

    :param specific_volume: Specific volume in atomic units.
    :param temperature: Temperature in atomic units.
    :param chemical_potential: Chemical potential in atomic units.
    :return: C_S[i][j] - C_S in atomic units. *i*-th index is for temperature, *j*-th one is for volume
    """
    y = np.multiply(chemical_potential.T, 1/temperature).T
    vv, tt = np.meshgrid(specific_volume, temperature)
    C_S = np.sqrt(10)*2**(1/4)/(3*np.pi) * tt**(5/4)*np.sqrt(vv*_1d_call(_fdk, y, k=3/2))
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
                    os.path.join(os.getcwd(), csv_dir, f'{key}_v={volume}_atomic_units.csv'),
                    np.array([temperature_range, properties[key][:, i]]).T)
    return properties
