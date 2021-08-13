from typing import Iterable

import numpy as np
import scipy.constants as const
from scipy.constants import physical_constants


class SiAtomicConverter:
    def __init__(self, from_si=True):
        """Class for converting from SI units to atomic (and visa versa)

        :param from_si: Whether to convert from SI or atomic
        """
        self.from_si = from_si
        # self.ab - Bohr radius
        self.ab = physical_constants["Bohr radius"][0]
        # self.ab3 - Bohr radius to the 3rd power
        self.ab3 = self.ab * self.ab * self.ab
        # self.ec = elementary charge
        self.ec = physical_constants["elementary charge"][0]
        # self.kb - Boltzmann constant
        self.kb = physical_constants["Boltzmann constant"][0]
        # self.e0 - Vacuum permeatbility
        self.e0 = physical_constants["electric constant"][0]
        # self.ha - Hartree energy in Joules
        self.ha = 0.25 * self.ec * self.ec / const.pi / self.e0 / self.ab

    def convert_energy(self, energy):
        """Converts energy.

        :param energy: Energy in corresponding units system
        :return: Converted energy
        """
        if self.from_si:
            return energy / self.ha * self.ab3
        else:
            return energy * self.ha / self.ab3

    def convert_temperature(self, temperature):
        """Converts temperature.

        :param temperature: Temperature in corresponding units system
        :return: Converted temperature
        """
        if self.from_si:
            return temperature / self.ha * self.kb
        else:
            # E_h -> Joules -> Kelvins
            return temperature * self.ha / self.kb

    def convert_volume(self, volume):
        """Converts volume.

        :param volume: Volume in corresponding units system
        :return: Converted volume
        """
        if self.from_si:
            return volume / self.ab3
        else:
            return volume * self.ab3

    def convert_pressure(self, pressure):
        """Converts pressure.

        :param pressure: Pressure in corresponding units system
        :return: Converted pressure
        """
        if self.from_si:
            return pressure / self.ha * self.ab3
        else:
            return pressure * self.ha / self.ab3

    def convert_entropy(self, entropy):
        """Converts entropy.

        :param entropy: Entropy in corresponding units system
        :return: Converted entropy
        """
        if self.from_si:
            return entropy / self.kb * self.ab3
        else:
            return entropy * self.kb / self.ab3

    def convert_heat_capacity(self, heat_capacity):
        """Converts heat_capacity.

        :param heat_capacity: Heat_capacity in corresponding units system
        :return: Converted heat_capacity
        """
        # Since entropy and heat capacity have same units
        return self.convert_entropy(heat_capacity)

    def convert_sound_speed(self, sound_speed):
        """Converts sound speed.

        :param sound_speed: Sound speed in corresponding units system
        :return: Converted sound speed
        """
        if self.from_si:
            return (
                sound_speed
                / physical_constants["atomic unit of length"][0]
                * physical_constants["atomic unit of time"][0]
            )
        else:
            return (
                sound_speed
                * physical_constants["atomic unit of length"][0]
                / physical_constants["atomic unit of time"][0]
            )

    # TODO: ignores `from_si` parameter


def convert_density(density_sgs, molar_mass_sgs):
    """
    Converts density from g/cm^3 to specific volume in SI using molar mass.
    NOTE: ignores `from_si` parameter

    :param density_sgs: g/cm^3
    :param molar_mass_sgs: g/mol
    :return: specific volume in SI, m^3
    """
    # Per one mol
    v_si = molar_mass_sgs / density_sgs / 10 ** 6
    # Per one particle
    v_si /= physical_constants["Avogadro constant"][0]
    return v_si


def get_metal_specific_volume(density_sgs, molar_mass_sgs, num_electrons):
    """Calculate metal's specific volume from its density, molar mass and
    number of electrons on outer shell.

    :param density_sgs: Density in g/cm^3
    :param molar_mass_sgs: Molar mass in g/mol
    :param num_electrons: Number of electrons on outer shell
    :return: Specific volume in SI
    """
    v = convert_density(density_sgs=density_sgs, molar_mass_sgs=molar_mass_sgs)
    v /= num_electrons
    return v


def convert_r_s_to_specific_volume(r_s):
    # type: (Iterable) -> np.array
    """Given formula
    4/3 pi (r_s)^3 = 1/n,
    convert r_s to specific volume.

    :param r_s:
    :return:
    """
    return 4 / 3 * np.pi * np.array(r_s) ** 3
