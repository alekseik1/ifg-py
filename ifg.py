from fdint import fdk, ifd1h
import numpy as np
from units_converter import SiAtomicConverter


def get_chemical_potential(specific_volume, temperature):
    """

    :param specific_volume: Specific volume in atomic units
    :param temperature: Temperature in atomic units
    :return: chemical potential in atomic units
    """
    g = 2
    gamma_32 = np.sqrt(np.pi)/2
    # TODO: опять подгоны. Не нужно делить на Г(3/2), у меня нет объяснений
    #to_inverse = np.sqrt(2)*np.pi**2 / (g * temperature ** (3 / 2) * specific_volume * gamma_32)
    to_inverse = np.sqrt(2)*np.pi**2 / (g * temperature ** (3 / 2) * specific_volume)
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
    import matplotlib.pyplot as plt
    converter = SiAtomicConverter(from_si=True)
    reverse_converter = SiAtomicConverter(from_si=False)
    # For Aluminium
    v_Al = converter.convert_density(density_sgs=2.70, molar_mass_sgs=26.98)
    # Since Aluminium has 3 electrons on valence shell
    v_Al /= 3
    T_range = np.arange(10**6, 10**8, 100)
    # Convert to atomic units
    v_Al = converter.convert_volume(v_Al)
    T_range = converter.convert_temperature(T_range)
    # TODO: refactor to something like `GasDescriber` that will take care of all plots
    ##################################################
    # For mu
    ##################################################
    # Calculate mu
    mu_range = get_chemical_potential(
        v_Al,
        T_range
    )
    plt.plot(T_range, mu_range/T_range)
    plt.title(r'$\mu (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$\mu, [E_h]$')
    plt.grid()
    plt.show()
    ##################################################
    # For pressure
    ##################################################
    # Calculate pressure
    p_range = get_pressure(
        temperature=T_range,
        chemical_potential=mu_range
    )
    plt.plot(T_range, p_range)
    plt.title(r'$p (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$p$, [atomic units]')
    plt.grid()
    plt.show()
    ##################################################
    # For entropy
    ##################################################
    S_range = get_entropy(
        specific_volume=v_Al,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plt.plot(T_range, S_range)
    plt.title(r'$S (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$S$')
    plt.grid()
    plt.show()
    ##################################################
    # For C_V
    ##################################################
    C_V_range = get_heat_capacity_volume(
        specific_volume=v_Al,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plt.plot(T_range, C_V_range)
    plt.title(r'$C_V (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$C_V$')
    plt.grid()
    plt.show()
    ##################################################
    # For C_P
    ##################################################
    C_P_range = get_heat_capacity_pressure(
        specific_volume=v_Al,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plt.plot(T_range, C_P_range)
    plt.title(r'$C_P (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$C_P$')
    plt.grid()
    plt.show()
    ##################################################
    # For C_T
    ##################################################
    C_T_range = get_sound_speed_temperature(
        specific_volume=v_Al,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plt.plot(T_range, C_T_range)
    plt.title(r'$C_T (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$C_T$, [atomic units]')
    plt.grid()
    plt.show()
    ##################################################
    # For C_S
    ##################################################
    C_S_range = get_sound_speed_entropy(
        specific_volume=v_Al,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plt.plot(T_range, C_S_range**2)
    plt.title(r'$C_S (v, T)$')
    plt.xlabel('T, atomic units')
    plt.ylabel(r'$C_S$, [atomic units]')
    plt.grid()
    plt.show()
