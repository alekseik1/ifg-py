from __future__ import division
import unittest
from ifg_py import SiAtomicConverter
from hypothesis import given
from hypothesis.strategies import floats

HARDCODED_TESTS = {
    # (SI, atomic, func_name)
    (2.9421912E+13, 1., 'convert_pressure'),
    (4.3597447222071E-18, 1., 'convert_energy'),
    (315774.64, 1., 'convert_temperature'),
    (5.29177E-11**3, 1., 'convert_volume'),
    (1.380649E-23, 1., 'convert_entropy'),
    (1.380649E-23, 1., 'convert_heat_capacity'),
    (5.29177210671212E-11/2.418884326509E-17, 1., 'convert_sound_speed'),
}


class ConverterTests(unittest.TestCase):

    def setUp(self):
        self.from_si = SiAtomicConverter(from_si=True)
        self.from_atomic = SiAtomicConverter(from_si=False)
        self.available_converters = filter(
            lambda x: 'convert_' in x,
            dir(SiAtomicConverter))

    def assertNearlyEqual(self, a, b, fraction=0.02):
        if abs(a - b) > abs(fraction * a):
            self.fail("The given numbers %s and %s are not near each other." % (a, b))

    @given(floats(min_value=10**-40))
    def test_inverse_conversion(self, nums):
        # Si -> Atomic -> Si gives same result
        for func_str in self.available_converters:
            from_si = getattr(self.from_si, func_str)
            from_atomic = getattr(self.from_atomic, func_str)
            self.assertNearlyEqual(from_si(from_atomic(nums)), nums)

    def test_hardcoded_values(self):
        for si_value, atomic_value, func_name in HARDCODED_TESTS:
            from_atomic = getattr(self.from_atomic, func_name)
            from_si = getattr(self.from_si, func_name)
            self.assertNearlyEqual(from_atomic(atomic_value), si_value)
            self.assertNearlyEqual(from_si(si_value), atomic_value)
