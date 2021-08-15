import numpy as np
import numpy.testing as npt
import pytest
from hypothesis import given, strategies as st
from pytest import approx

from ifg.units_converter import (
    convert_r_s_to_specific_volume,
    convert_theta_to_temperature,
)

allowed_numbers = st.floats(min_value=1e-50, max_value=1e50)
# One in atomic is `atomic_to_si[quantity]` in SI
atomic_to_si = {
    "pressure": 29421015696686.086,
    # NOTE: energy is relative to volume, i.e. J / m^3
    "energy": 4.3597447222071e-18 / (5.29177210903 * 10 ** -11) ** 3,
    "temperature": 315775.02480232634,
    "volume": 1.481847114721628e-31,
    # NOTE: energy is relative to volume, i.e. J / m^3
    "entropy": 1.380649e-23 / (5.29177210903 * 10 ** -11) ** 3,
    # NOTE: energy is relative to volume, i.e. J / m^3
    "heat_capacity": 1.380649e-23 / (5.29177210903 * 10 ** -11) ** 3,
    "sound_speed": 2187691.2636411325,
}


@given(allowed_numbers)
def test_to_and_back_are_equal(quantity, from_si_converter, to_si_converter, value):
    converted = getattr(from_si_converter, "convert_{}".format(quantity))(value)
    original = getattr(to_si_converter, "convert_{}".format(quantity))(converted)
    assert value == approx(original)


@given(allowed_numbers)
def test_correct_from_atomic(quantity, to_si_converter, value):
    converted = getattr(to_si_converter, "convert_{}".format(quantity))(value)
    assert converted == approx(value * atomic_to_si[quantity])


@given(allowed_numbers)
def test_correct_from_si(quantity, from_si_converter, value):
    converted = getattr(from_si_converter, "convert_{}".format(quantity))(value)
    assert converted == approx(value / atomic_to_si[quantity])


@pytest.mark.parametrize(
    "r_s, v",
    [
        ([1.0], [4 / 3 * np.pi]),
        ([2.0, 3.0], 4 / 3 * np.pi * np.array([2.0, 3.0]) ** 3),
    ],
)
def test_correct_from_r_s_to_specific_volume(r_s, v):
    # GIVEN: sample r_s value (unit system does not matter)
    # WHEN: r_s value is converted to specific volume
    # THEN: the result equals to the expected one
    assert convert_r_s_to_specific_volume(r_s) == approx(v)


class TestConverterFromThetaToTemperature:
    @pytest.mark.parametrize(
        "theta, volume, temperature",
        [
            ([1.0], 2.0, [[3.014607]]),
            ([3.0], 5.0, [[4.909741]]),
            ([3.0, 5.0], 5.0, [[4.909741, 8.182902]]),
            ([3.0, 5.0], [5.0, 10.0], [[4.909741, 8.182902], [3.092943, 5.154905]]),
        ],
    )
    def test_correct_conversion(self, theta, volume, temperature):
        # GIVEN: theta and specific volume (atomic)
        # WHEN: conversion to temperature occurs
        # THEN: the result equals to the expected one
        npt.assert_allclose(convert_theta_to_temperature(theta, volume), temperature)
