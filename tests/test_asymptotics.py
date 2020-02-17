import unittest
import numpy as np
from scipy.constants import k
from ifg_py import IfgCalculator, get_metal_specific_volume


class AsymptoticTest(unittest.TestCase):

    def setUp(self):
        self.v_range = np.array([
            get_metal_specific_volume(
                density_sgs=2.70, molar_mass_sgs=26.98, num_electrons=3
            ),
        ])
        self.temparatures = np.arange(10**10 - 10**8, 10**10)
        self.calculator = IfgCalculator(
            input_in_si=True, output_in_si=True,
            specific_volumes=self.v_range,
            temperatures=self.temparatures)

    def assertNearlyEqual(self, a, b, fraction=0.02):
        if abs(a - b) > abs(fraction * a):
            self.fail("The given numbers %s and %s are not near each other." % (a, b))

    def test_hardcoded(self):
        # For Cp and Cv
        HARDCODED_ASYMPTOTICS_SI = {
            # (expected in SI per atom, func name)
            # Only 1-dimensional, no arrays (we do simple tests)
            (lambda v, T: 5/2*k, 'get_heat_capacity_pressure'),
            (lambda v, T: 3/2*k, 'get_heat_capacity_volume'),
        }
        for expected_si, func_name in HARDCODED_ASYMPTOTICS_SI:
            func = getattr(self.calculator, func_name)
            calculated = func()
            self.assertNearlyEqual(expected_si(self.v_range[-1], self.temparatures[-1]),
                                   calculated[-1, -1])
