import hypothesis.extra.numpy as st_numpy
from hypothesis import strategies as st, given
import numpy as np
from ifg_py import IfgCalculator


g = 2
A = 3/5*(3*np.pi**2/(np.sqrt(2)*g))**(2/3)
beta = (g*np.pi/6)**(2/3)


temperatures_st = st_numpy.arrays(np.float, st.tuples(st.integers(0, 100)),
                                  elements=st.floats(1E-49, 1E-30))
volumes_st = st_numpy.arrays(np.float, st.tuples(st.integers(1, 1)),
                             elements=st.floats(10., 100.))


class TestLowTemperaturesLimits:

    @given(temperatures_st, volumes_st)
    def test_chemical_potential(self, temperatures, volumes):
        calculator = IfgCalculator(
            temperatures=temperatures,
            specific_volumes=volumes,
            input_in_si=False,
            output_in_si=False
        )
        vv, tt = np.meshgrid(volumes, temperatures)
        # According to the original article
        eps_F = (3*np.pi**2/(np.sqrt(2)*g*vv))**(2/3)
        expected = eps_F*(1 - np.pi**2 / 12 * (tt/eps_F)**2)
        np.testing.assert_array_almost_equal(calculator.mu, expected)

    @given(temperatures_st, volumes_st)
    def test_pressure(self, temperatures, volumes):
        calculator = IfgCalculator(
            temperatures=temperatures,
            specific_volumes=volumes,
            input_in_si=False,
            output_in_si=False
        )
        vv, tt = np.meshgrid(volumes, temperatures)
        # According to the original article
        expected = 2 / 3 * A * vv ** (-5 / 3) + beta / 3 * tt ** 2 * vv ** (2 / 3)
        np.testing.assert_array_almost_equal(calculator.p, expected)
