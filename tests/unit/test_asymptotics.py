from __future__ import division
from hypothesis import given, settings
from datetime import timedelta
import numpy as np
from tests.conftest import volumes_st, temperatures_st, temperatures_high, set_up

g = 2
A = 3/5*(3*np.pi**2/(np.sqrt(2)*g))**(2/3)
beta = (g*np.pi/6)**(2/3)


class TestLowTemperaturesLimits:

    @given(temperatures_st, volumes_st)
    def test_entropy(self, temps, vols):
        with set_up(temps, vols) as (calculator, (vv, tt)):
            expected = beta * tt * vv**(2/3)
            np.testing.assert_allclose(calculator.S, expected)

    @given(temperatures_st, volumes_st)
    def test_C_V(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = beta * tt * vv**(2/3)
            np.testing.assert_allclose(calc.C_V, expected)

    @given(temperatures_st, volumes_st)
    @settings(deadline=timedelta(seconds=1))
    def test_C_P(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = beta * tt * vv**(2/3)
            np.testing.assert_allclose(calc.C_P, expected)

    @given(temperatures_st, volumes_st)
    def test_C_T(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = np.sqrt(10/9 * A * vv**(-2/3) + beta/9 * tt**2 * vv**(2/3))
            np.testing.assert_allclose(calc.C_T, expected)

    @given(temperatures_st, volumes_st)
    def test_C_S(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = np.sqrt(10/9 * A * vv**(-2/3) + 5/9 * beta * tt**2 * vv**(2/3))
            np.testing.assert_allclose(calc.C_S, expected)

    @given(temperatures_st, volumes_st)
    def test_F_potential(self, temps, vols):
        with set_up(temps, vols) as (calculator, (vv, tt)):
            expected = A*vv**(-2/3) - beta/2 * tt**2 * vv**(2/3)
            np.testing.assert_allclose(calculator.F, expected)

    @given(temperatures_st, volumes_st)
    def test_chemical_potential(self, temperatures, volumes):
        with set_up(temperatures, volumes) as (calculator, (vv, tt)):
            # According to the original article
            eps_F = (3*np.pi**2/(np.sqrt(2)*g*vv))**(2/3)
            expected = eps_F*(1 - np.pi**2 / 12 * (tt/eps_F)**2)
            np.testing.assert_allclose(calculator.mu, expected)

    @given(temperatures_st, volumes_st)
    def test_pressure(self, temperatures, volumes):
        with set_up(temperatures, volumes) as (calculator, (vv, tt)):
            # According to the original article
            expected = 2 / 3 * A * vv ** (-5 / 3) + beta / 3 * tt ** 2 * vv ** (2 / 3)
            np.testing.assert_allclose(calculator.p, expected)


class TestHighTemperaturesLimits:

    @given(temperatures_high, volumes_st)
    def test_pressure(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = tt/vv
            np.testing.assert_allclose(calc.p, expected)

    @given(temperatures_high, volumes_st)
    def test_chemical_potential(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = tt * np.log(1/(g*vv) * (2*np.pi/tt)**(3/2))
            np.testing.assert_allclose(calc.mu, expected)

    @given(temperatures_high, volumes_st)
    def test_F_potential(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = tt * np.log(1/(g*vv) * (2*np.pi/tt)**(3/2)) - tt \
                       + np.pi**(3/2) / (2*g*vv*tt**(1/2))
            np.testing.assert_allclose(calc.F, expected)

    @given(temperatures_high, volumes_st)
    def test_C_S(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = np.sqrt(5/3*tt)
            np.testing.assert_allclose(calc.C_S, expected)

    @given(temperatures_high, volumes_st)
    def test_C_T(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = np.sqrt(tt)
            np.testing.assert_allclose(calc.C_T, expected)

    @given(temperatures_high, volumes_st)
    def test_C_P(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = 5/2*np.ones_like(tt)
            np.testing.assert_allclose(calc.C_P, expected)

    @given(temperatures_high, volumes_st)
    def test_C_V(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = 3/2*np.ones_like(tt)
            np.testing.assert_allclose(calc.C_V, expected)

    @given(temperatures_high, volumes_st)
    def test_entropy(self, temps, vols):
        with set_up(temps, vols) as (calc, (vv, tt)):
            expected = 5/2 - calc.mu / tt
            np.testing.assert_allclose(calc.S, expected)
