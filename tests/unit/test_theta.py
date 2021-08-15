import numpy as np
import pytest
from numpy import testing as npt

from ifg.calculator import _make_mesh
from ifg.units_converter import convert_theta_to_temperature

COMPLICATED_MESH = (
    [3.0, 5.0],
    [5.0, 10.0, 15.0],
    np.array(
        [
            [4.909741, 8.182902],
            [3.092943, 5.154905],
            [2.36035732, 3.9339289],
        ]
    ),
)


@pytest.fixture(
    params=[
        ([1.0], 2.0, np.array([[3.014607]])),
        ([3.0], 5.0, np.array([[4.909741]])),
        ([3.0, 5.0], 5.0, np.array([[4.909741, 8.182902]])),
        COMPLICATED_MESH,
    ],
)
def mesh_example(request):
    return request.param


class TestConverterFromThetaToTemperature:
    def test_correct_conversion(self, mesh_example):
        theta, volume, temperature = mesh_example
        # GIVEN: theta and specific volume (atomic)
        # WHEN: conversion to temperature occurs
        # THEN: the result equals to the expected one
        npt.assert_allclose(convert_theta_to_temperature(theta, volume), temperature)


def test_correct_mesh_creation():
    theta, volume, temperature = COMPLICATED_MESH
    vv, tt = _make_mesh(volume, temperature)
    npt.assert_allclose(vv, [[5.0, 10.0, 15.0], [5.0, 10.0, 15.0]])
    npt.assert_allclose(
        tt,
        np.array(
            [
                [4.909741, 8.182902],  # for volume=5.0
                [3.092943, 5.154905],  # for volume=10.0
                [2.36035732, 3.9339289],  # for volume=15.0
            ]
        ),
    )
