import numpy as np
import pytest
from numpy import testing as npt

from ifg.calculator import IfgCalculator
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


@pytest.mark.skip("broken after input methods refactoring")
def test_correct_mesh_creation():
    # GIVEN: theta array, volume array and corresponding temperatures
    theta, volume, temperature = COMPLICATED_MESH
    # WHEN: mesh is created upon these volumes and temperatures
    vv, tt = _make_mesh(volume, temperature)
    # THEN: volume grid is created as if w/o theta
    npt.assert_allclose(
        vv,
        [
            [5.0, 10.0, 15.0],
            [5.0, 10.0, 15.0],
        ],
    )
    # THEN: temperature grid is created with respect to both volumes and thetas
    npt.assert_allclose(
        tt,
        np.array(
            [
                [4.909741, 3.092943, 2.36035732],
                [8.182902, 5.154905, 3.9339289],
            ]
        ),
    )


@pytest.mark.skip("broken after input methods refactoring")
def test_correct_simple_mesh_creation():
    from ifg.calculator import _make_mesh

    # GIVEN: simple (non-theta) volumes and temperatures
    volumes = [1.0, 2.0]
    temperatures = [10.0, 20.0, 30.0]
    # WHEN: mesh grid is created
    vv, tt = _make_mesh(volumes, temperatures)
    # THEN: correct simple mesh is created
    npt.assert_allclose(vv, [[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
    npt.assert_allclose(tt, [[10.0, 10.0], [20.0, 20.0], [30.0, 30.0]])


@pytest.mark.skip("broken after with_ removal")
def test_cannot_input_theta_before_volume():
    # GIVEN: freshly created IfgCalculator()
    # WHEN: `with_theta` is called before volume input
    # THEN: exception is raised
    with pytest.raises(ValueError) as e:
        IfgCalculator().with_theta([1.0, 2.0])
        assert e.match(
            "specific volume should be defined before using theta for temperature input"
        )
