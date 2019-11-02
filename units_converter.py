from scipy.constants import physical_constants


class SiAtomicConverter:

    def __init__(self, from_si=True):
        self.from_si = from_si

    def convert_energy(self, energy):
        if self.from_si:
            return energy/physical_constants['atomic unit of energy'][0]
        else:
            return energy*physical_constants['atomic unit of energy'][0]

    def convert_temperature(self, temperature):
        if self.from_si:
            temperature_joule = temperature*physical_constants['kelvin-joule relationship'][0]
            return temperature_joule*physical_constants['joule-hartree relationship'][0]
        else:
            # E_h -> Joules -> Kelvins
            temperature_joule = temperature*physical_constants['hartree-joule relationship'][0]
            return temperature_joule*physical_constants['joule-kelvin relationship'][0]

    def convert_volume(self, volume):
        if self.from_si:
            return volume/physical_constants['atomic unit of length'][0]**3
        else:
            return volume*physical_constants['atomic unit of length'][0]**3

    def convert_pressure(self, pressure):
        if self.from_si:
            return pressure/physical_constants['atomic unit of force'][0] * \
                   physical_constants['atomic unit of length'][0]**2
        else:
            return pressure*physical_constants['atomic unit of force'][0] / \
                   physical_constants['atomic unit of length'][0]**2

    def convert_entropy(self, entropy):
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
        # Since entropy and heat capacity have same units
        return self.convert_entropy(heat_capacity)

    def convert_sound_speed(self, sound_speed):
        if self.from_si:
            return sound_speed/physical_constants['atomic unit of length'][0] * \
                   physical_constants['atomic unit of time'][0]
        else:
            return sound_speed*physical_constants['atomic unit of length'][0] / \
                   physical_constants['atomic unit of time'][0]

    # TODO: ignores `from_si` parameter
    def convert_density(self, density_sgs, molar_mass_sgs):
        """

        :param density_sgs: g/cm^3
        :param molar_mass_sgs: g/mol
        :return: specific volume in SI
        """
        # Per one mol
        v_si = molar_mass_sgs/density_sgs / 10**6
        # Per one particle
        v_si /= physical_constants['Avogadro constant'][0]
        return v_si
