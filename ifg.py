from fdint import fdk, ifd1h
import numpy as np
from scipy.special import gamma


def get_chemical_potential(specific_volume, temperature):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :return: chemical potential in atomic units
    """
    g = 2
    gamma_32 = np.sqrt(np.pi)/2
    to_inverse = np.sqrt(2)*np.pi**2 / (g * temperature ** (3 / 2) * specific_volume * gamma_32)
    mu_T = ifd1h(to_inverse)
    mu = mu_T * temperature
    return mu


def get_F_potential(specific_volume, temperature, chemical_potential):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: Helmholtz free energy in atomic units
    """
    y = chemical_potential/temperature
    F = np.sqrt(2)/np.pi**2 * temperature**(5/2)*specific_volume*(y*fdk(1/2, y) - 2/3*fdk(3/2, y))
    return F


def get_pressure(temperature, chemical_potential):
    """

    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: Pressure in atomic units
    """
    y = chemical_potential/temperature
    pressure = 2*np.sqrt(2)/(3*np.pi**2) * temperature**(5/2)*fdk(3/2, y)
    return pressure


def get_entropy(specific_volume, temperature, chemical_potential):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: Entropy in atomic units
    """
    y = chemical_potential/temperature
    S = -np.sqrt(2)/(3*np.pi**2) * temperature**(3/2)*specific_volume*(3*y*fdk(1/2, y) - 5*fdk(3/2, y))
    return S


def get_heat_capacity_volume(specific_volume, temperature, chemical_potential):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: C_V in atomic units
    """
    y = chemical_potential/temperature
    C_V = np.sqrt(2)/(2*np.pi**2) * temperature**(3/2)*specific_volume *\
          (5*fdk(-1/2, y)*fdk(3/2, y) - 9*fdk(1/2, y)**2)/fdk(-1/2, y)
    return C_V


def get_heat_capacity_pressure(specific_volume, temperature, chemical_potential):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: C_P in atomic units
    """
    y = chemical_potential/temperature
    C_P = 5*np.sqrt(2)/(18*np.pi**2) * temperature**(3/2)*specific_volume * \
          (5*fdk(-1/2, y)*fdk(3/2, y) - 9*fdk(1/2, y)**2)*fdk(3/2, y)/fdk(1/2, y)**2
    return C_P


def get_sound_speed_temperature(specific_volume, temperature, chemical_potential):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: C_T in atomic units
    """
    y = chemical_potential/temperature
    C_T = 2**(3/4)/np.pi * np.sqrt(specific_volume)*temperature**(5/4)*fdk(1/2, y) / np.sqrt(fdk(-1/2, y))
    return C_T


def get_sound_speed_entropy(specific_volume, temperature, chemical_potential):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :param chemical_potential: Chemical potential in atomic units
    :return: C_S in atomic units
    """
    y = chemical_potential/temperature
    C_S = np.sqrt(10)*2**(1/4)/(3*np.pi) * temperature**(5/4)*np.sqrt(specific_volume*fdk(3/2, y))
    return C_S


if __name__ == '__main__':
    pass
