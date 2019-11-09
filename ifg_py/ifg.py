from fdint import fdk, ifd1h
import numpy as np


def _1d_call(func, array, *args, **kwargs):
    return func(array.reshape(-1), *args, **kwargs).reshape(array.shape)


def _fdk(array, k):
    return fdk(k, array)


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
                             chemical_potential: np.ndarray, *args, **kwargs):
    """
    Get IFG heat capacity C_V in atomic units

    :param specific_volume: Specific volume in atomic units. **Note**: only one parameter can be numpy vector!
    :param temperature: Temperature in atomic units. **Note**: only one parameter can be numpy vector!
    :param chemical_potential: Chemical potential in atomic units. **Note**: only one parameter can be numpy vector!
    :return: C_V in atomic units
    """
    y = chemical_potential/temperature
    C_V = np.sqrt(2)/(2*np.pi**2) * temperature**(3/2)*specific_volume *\
          (5*fdk(-1/2, y)*fdk(3/2, y) - 9*fdk(1/2, y)**2)/fdk(-1/2, y)
    return C_V


def get_heat_capacity_pressure(specific_volume: np.ndarray, temperature: np.ndarray,
                               chemical_potential: np.ndarray, *args, **kwargs):
    """
    Get IFG heat capacity C_P in atomic units

    :param specific_volume: Specific volume in atomic units. **Note**: only one parameter can be numpy vector!
    :param temperature: Temperature in atomic units. **Note**: only one parameter can be numpy vector!
    :param chemical_potential: Chemical potential in atomic units. **Note**: only one parameter can be numpy vector!
    :return: C_P in atomic units
    """
    y = chemical_potential/temperature
    C_P = 5*np.sqrt(2)/(18*np.pi**2) * temperature**(3/2)*specific_volume * \
          (5*fdk(-1/2, y)*fdk(3/2, y) - 9*fdk(1/2, y)**2)*fdk(3/2, y)/fdk(1/2, y)**2
    return C_P


def get_sound_speed_temperature(specific_volume: np.ndarray, temperature: np.ndarray,
                                chemical_potential: np.ndarray, *args, **kwargs):
    """
    Get IFG sound speed C_T in atomic units

    :param specific_volume: Specific volume in atomic units. **Note**: only one parameter can be numpy vector!
    :param temperature: Temperature in atomic units. **Note**: only one parameter can be numpy vector!
    :param chemical_potential: Chemical potential in atomic units. **Note**: only one parameter can be numpy vector!
    :return: C_T in atomic units
    """
    y = chemical_potential/temperature
    C_T = 2**(3/4)/np.pi * np.sqrt(specific_volume)*temperature**(5/4)*fdk(1/2, y) / np.sqrt(fdk(-1/2, y))
    return C_T


def get_sound_speed_entropy(specific_volume: np.ndarray, temperature: np.ndarray,
                            chemical_potential: np.ndarray, *args, **kwargs):
    """
    Get IFG sound speed C_S in atomic units

    :param specific_volume: Specific volume in atomic units. **Note**: only one parameter can be numpy vector!
    :param temperature: Temperature in atomic units. **Note**: only one parameter can be numpy vector!
    :param chemical_potential: Chemical potential in atomic units. **Note**: only one parameter can be numpy vector!
    :return: C_S in atomic units
    """
    y = chemical_potential/temperature
    C_S = np.sqrt(10)*2**(1/4)/(3*np.pi) * temperature**(5/4)*np.sqrt(specific_volume*fdk(3/2, y))
    return C_S
