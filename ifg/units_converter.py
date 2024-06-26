import numpy as np

PI = 3.141592653589793
BOHR_RADIUS = 5.29177210903e-11
ELEMENTARY_CHARGE = 1.602176634e-19
BOLTZMANN_CONSTANT = 1.380649e-23
ELECTRIC_CONSTANT = 8.8541878128e-12
ATOMIC_UNIT_OF_LENGTH = 5.29177210903e-11
ATOMIC_UNIT_OF_TIME = 2.4188843265857e-17
AVOGADRO_CONSTANT = 6.02214076e+23


class SiAtomicConverter:
    def __init__(self, from_si=True):
        """Class for converting from SI units to atomic (and visa versa)

        :param from_si: Whether to convert from SI or atomic
        """
        self.from_si = from_si
        # self.ab - Bohr radius
        self.ab = BOHR_RADIUS
        # self.ab3 - Bohr radius to the 3rd power
        self.ab3 = self.ab * self.ab * self.ab
        # self.ec = elementary charge
        self.ec = ELEMENTARY_CHARGE
        # self.kb - Boltzmann constant
        self.kb = BOLTZMANN_CONSTANT
        # self.e0 - Vacuum permeatbility
        self.e0 = ELECTRIC_CONSTANT
        # self.ha - Hartree energy in Joules
        self.ha = 0.25 * self.ec * self.ec / PI / self.e0 / self.ab

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
            return sound_speed / ATOMIC_UNIT_OF_LENGTH * ATOMIC_UNIT_OF_TIME
        else:
            return sound_speed * ATOMIC_UNIT_OF_LENGTH / ATOMIC_UNIT_OF_TIME

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
    v_si = molar_mass_sgs / density_sgs / 10**6
    # Per one particle
    v_si /= AVOGADRO_CONSTANT
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


def convert_theta_to_temperature(theta, volumes):
    # type: (Union[Iterable, float], Union[Iterable, float]) -> np.ndarray
    """Convert theta to temperature in atomic units using formula:

    T = theta/2 * (3 pi^2 * 1/v)^(2/3)

    where k = (3 pi^2 * 1/v)^(1/3) is a Fermi wavevector.

    The volume should be in atomic units
    """
    tt, vv = np.meshgrid(theta, volumes)
    # 2-d array
    return tt / 2. * (3 * np.pi**2 / vv) ** (2. / 3)
