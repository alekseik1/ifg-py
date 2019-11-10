from ifg_py import get_chemical_potential, get_pressure, get_entropy, get_heat_capacity_volume, \
    get_heat_capacity_pressure, get_sound_speed_temperature, get_sound_speed_entropy, get_F_potential
from ifg_py import SiAtomicConverter
import numpy as np
import os


def describe_gas(specific_volume, temperature_range, plot_dir='plots'):
    """
    Fully describes a gas and plots graphs

    :param specific_volume: in atomic units
    :param temperature_range: in atomic units
    :param plot_dir: directory to save plots to
    :return:
    """
    ##################################################
    # For mu
    ##################################################
    # Calculate mu
    mu_range = get_chemical_potential(
        specific_volume,
        temperature_range
    )
    plot_values(
        x_values=temperature_range,
        y_values=mu_range / temperature_range,
        x_label=r'T, $E_h$',
        y_label=r'$\mu/T$',
        title=r'Chemical potential divided by temperature',
        plot_dir=plot_dir
    )
    plot_values(
        x_values=temperature_range,
        y_values=mu_range,
        x_label=r'T, $E_h$',
        y_label=r'$\mu$',
        title=r'Chemical potential',
        plot_dir=plot_dir
    )
    ##################################################
    # For pressure
    ##################################################
    # Calculate pressure
    p_range = get_pressure(
        temperature=temperature_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=temperature_range,
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
        temperature=temperature_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=temperature_range,
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
        temperature=temperature_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=temperature_range,
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
        temperature=temperature_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=temperature_range,
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
        temperature=temperature_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=temperature_range,
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
        temperature=temperature_range,
        chemical_potential=mu_range
    )
    plot_values(
        x_values=temperature_range,
        y_values=C_S_range**2,
        x_label=r'T, $E_h$',
        y_label=r'$C_S^2$',
        title=r'Speed of sound $C_S^2$',
        plot_dir=plot_dir
    )


def plot_values(x_values, y_values, x_label=None, y_label=None, title=None, plot_dir='plots'):
    """
    Plot graphs

    :param x_values: Values for x axis
    :param y_values: Values for y axis
    :param x_label: Label for x axis
    :param y_label: Label for y axis
    :param title: Title for graph
    :param plot_dir: Directory to save graphs to
    :return:
    """
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
    plt.clf()


def calculate_all_properties(specific_volume: np.ndarray, temperature_range: np.ndarray, csv_dir: str):
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
        for i, volume in enumerate(specific_volume):
            dump_to_csv(os.path.join(os.getcwd(), csv_dir, f'{key}_v={volume}_atomic_units.csv'),
                        np.array([temperature_range, properties[key][:, i]]).T)
    return properties


def dump_to_csv(filepath, data):
    """
    Dumps `data` to csv under `filepath`. Creates all necessary folders
    :param filepath: Path to file, like 'data/1.csv'
    :param data: Data to dump
    :return:
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, sep=';')


if __name__ == '__main__':
    converter = SiAtomicConverter(from_si=True)
    reverse_converter = SiAtomicConverter(from_si=False)
    # For Aluminium
    v_Al = converter.convert_density(density_sgs=2.70, molar_mass_sgs=26.98)
    # Since Aluminium has 3 electrons on valence shell
    v_Al /= 3
    v_Al = converter.convert_volume(v_Al)
    v_Cu = converter.convert_density(density_sgs=8.92, molar_mass_sgs=63.5)
    v_Cu /= 2
    v_Cu = converter.convert_volume(v_Cu)
    print('v_Al:', v_Al, '\n', 'v_Cu:', v_Cu)
    v_array = np.array([v_Al, v_Cu])

    T_range = np.hstack((
        np.arange(10**0, 10**4, 10),
        np.arange(10**4, 10**8, 1000),
    ))
    T_range = converter.convert_temperature(T_range)
    high_properties = calculate_all_properties(v_array, T_range, 'data/all_temperatures')
