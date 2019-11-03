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


def plot_values(x_values, y_values, x_label=None, y_label=None, title=None, plot_dir='plots'):
    import matplotlib.pyplot as plt
    import os
    plot_dir = os.path.join(os.curdir, plot_dir)
    os.makedirs(plot_dir, exist_ok=True)
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.savefig(os.path.join(plot_dir, f'{title}.pdf'))
    plt.show()


def describe_gas(specific_volume, T_range, plot_dir='plots'):
    """
    Fully describes a gas and plots graphs
    :param specific_volume: in atomic units
    :param T_range: in atomic units
    :return:
    """
    ##################################################
    # For mu
    ##################################################
    # Calculate mu
    mu_range = get_chemical_potential(
        specific_volume,
        T_range
    )
    plot_values(
        x_values=T_range,
        y_values=mu_range/T_range,
        x_label=r'T, $E_h$',
        y_label=r'$\mu/T$',
        title=r'Chemical potential divided by temperature',
        plot_dir=plot_dir
    )
    ##################################################
    # For pressure
    ##################################################
    # Calculate pressure
    p_range = get_pressure(
        temperature=T_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=T_range,
        y_values=p_range,
        x_label=r'T, $E_h$',
        y_label=r'$p$, atomic units',
        title=r'Pressure',
        plot_dir=plot_dir
    )
    ##################################################
    # For entropy
    ##################################################
    S_range = get_entropy(
        specific_volume=specific_volume,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=T_range,
        y_values=S_range,
        x_label=r'T, $E_h$',
        y_label=r'$S$',
        title=r'Entropy',
        plot_dir=plot_dir
    )
    ##################################################
    # For C_V
    ##################################################
    C_V_range = get_heat_capacity_volume(
        specific_volume=specific_volume,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=T_range,
        y_values=C_V_range,
        x_label=r'T, $E_h$',
        y_label=r'$C_V$',
        title=r'Heat capacity $C_V$',
        plot_dir=plot_dir
    )
    ##################################################
    # For C_P
    ##################################################
    C_P_range = get_heat_capacity_pressure(
        specific_volume=specific_volume,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=T_range,
        y_values=C_P_range,
        x_label=r'T, $E_h$',
        y_label=r'$C_P$',
        title=r'Heat capacity $C_P$',
        plot_dir=plot_dir
    )
    ##################################################
    # For C_T
    ##################################################
    C_T_range = get_sound_speed_temperature(
        specific_volume=specific_volume,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=T_range,
        y_values=C_T_range**2,
        x_label=r'T, $E_h$',
        y_label=r'$C_T^2$',
        title=r'Speed of sound $C_T^2$',
        plot_dir=plot_dir
    )
    ##################################################
    # For C_S
    ##################################################
    C_S_range = get_sound_speed_entropy(
        specific_volume=specific_volume,
        temperature=T_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=T_range,
        y_values=C_S_range**2,
        x_label=r'T, $E_h$',
        y_label=r'$C_S^2$',
        title=r'Speed of sound $C_S^2$',
        plot_dir=plot_dir
    )


if __name__ == '__main__':
    converter = SiAtomicConverter(from_si=True)
    reverse_converter = SiAtomicConverter(from_si=False)
    # For Aluminium
    v_Al = converter.convert_density(density_sgs=2.70, molar_mass_sgs=26.98)
    # Since Aluminium has 3 electrons on valence shell
    v_Al /= 3
    v_Al = converter.convert_volume(v_Al)

    # High temperatures
    T_range = np.arange(10**6, 10**8, 100)
    T_range = converter.convert_temperature(T_range)
    describe_gas(specific_volume=v_Al, T_range=T_range, plot_dir='T=10^6..10^8')

    T_range = np.arange(10**0, 10**4, 100)
    T_range = converter.convert_temperature(T_range)
    describe_gas(specific_volume=v_Al, T_range=T_range, plot_dir='T=10^0..10^4')

