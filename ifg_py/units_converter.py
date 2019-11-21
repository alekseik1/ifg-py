from scipy.constants import physical_constants


class SiAtomicConverter:

    def __init__(self, from_si=True):
        """
        Class for converting from SI units to atomic (and visa versa)

        :param from_si: Whether to convert from SI or atomic
        """
        self.from_si = from_si

    def convert_energy(self, energy):
        """
        Converts energy (from SI or atomic, depends on `from_si` flag in class constructor)

        :param energy: Energy in corresponding units system
        :return: Converted energy
        """
        if self.from_si:
            return energy/physical_constants['atomic unit of energy'][0]
        else:
            return energy*physical_constants['atomic unit of energy'][0]

    def convert_temperature(self, temperature):
        """
        Converts temperature (from SI or atomic, depends on `from_si` flag in class constructor)

        :param temperature: Temperature in corresponding units system
        :return: Converted temperature
        """
        if self.from_si:
            temperature_joule = temperature*physical_constants['kelvin-joule relationship'][0]
            return temperature_joule*physical_constants['joule-hartree relationship'][0]
        else:
            # E_h -> Joules -> Kelvins
            temperature_joule = temperature*physical_constants['hartree-joule relationship'][0]
            return temperature_joule*physical_constants['joule-kelvin relationship'][0]

    def convert_volume(self, volume):
        """
        Converts volume (from SI or atomic, depends on `from_si` flag in class constructor)

        :param volume: Volume in corresponding units system
        :return: Converted volume
        """
        if self.from_si:
            return volume/physical_constants['atomic unit of length'][0]**3
        else:
            return volume*physical_constants['atomic unit of length'][0]**3

    def convert_pressure(self, pressure):
        """
        Converts pressure (from SI or atomic, depends on `from_si` flag in class constructor)

        :param pressure: Pressure in corresponding units system
        :return: Converted pressure
        """
        if self.from_si:
            return pressure/physical_constants['atomic unit of force'][0] * \
                   physical_constants['atomic unit of length'][0]**2
        else:
            return pressure*physical_constants['atomic unit of force'][0] / \
                   physical_constants['atomic unit of length'][0]**2

    def convert_entropy(self, entropy):
        """
        Converts entropy (from SI or atomic, depends on `from_si` flag in class constructor)

        :param entropy: Entropy in corresponding units system
        :return: Converted entropy
        """
        if self.from_si:
            # Convert joules
            tmp = entropy*physical_constants['joule-hartree relationship'][0]
            # Convert temperature
            coeff = physical_constants['kelvin-joule relationship'][0] * \
                    physical_constants['joule-hartree relationship'][0]
            tmp /= coeff
            return tmp
        else:
            # Convert joules
            tmp = entropy/physical_constants['joule-hartree relationship'][0]
            # Convert temperature
            coeff = physical_constants['kelvin-joule relationship'][0] * \
                    physical_constants['joule-hartree relationship'][0]
            tmp *= coeff
            return tmp

    def convert_heat_capacity(self, heat_capacity):
        """
        Converts heat_capacity (from SI or atomic, depends on `from_si` flag in class constructor)

        :param heat_capacity: Heat_capacity in corresponding units system
        :return: Converted heat_capacity
        """
        # Since entropy and heat capacity have same units
        return self.convert_entropy(heat_capacity)

    def convert_sound_speed(self, sound_speed):
        """
        Converts sound speed (from SI or atomic, depends on `from_si` flag in class constructor)

        :param sound_speed: Sound speed in corresponding units system
        :return: Converted sound speed
        """
        if self.from_si:
            return sound_speed/physical_constants['atomic unit of length'][0] * \
                   physical_constants['atomic unit of time'][0]
        else:
            return sound_speed*physical_constants['atomic unit of length'][0] / \
                   physical_constants['atomic unit of time'][0]

    # TODO: ignores `from_si` parameter
    def convert_density(self, density_sgs, molar_mass_sgs):
        """
        Converts density from g/cm^3 to specific volume in SI using molar mass

        :param density_sgs: g/cm^3
        :param molar_mass_sgs: g/mol
        :return: specific volume in SI
        """
        # Per one mol
        v_si = molar_mass_sgs/density_sgs / 10**6
        # Per one particle
        v_si /= physical_constants['Avogadro constant'][0]
        return v_si


def get_metal_specific_volume(density_sgs: float, molar_mass_sgs: float, num_electrons: float) -> float:
    """
    Calculate metal's specific volume from its density, molar mass and number of electrons on outer shell

    :param density_sgs: Density in g/cm^3
    :param molar_mass_sgs: Molar mass in g/mol
    :param num_electrons: Number of electrons on outer shell
    :return: Specific volume in atomic units
    """
    converter = SiAtomicConverter(from_si=True)
    v = converter.convert_density(density_sgs=density_sgs, molar_mass_sgs=molar_mass_sgs)
    v /= num_electrons
    return converter.convert_volume(v)

