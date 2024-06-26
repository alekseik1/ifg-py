from contextlib import contextmanager
from datetime import timedelta

import numpy as np
import pytest
from hypothesis import settings, strategies as st
from hypothesis.extra import numpy as st_numpy

from ifg import IfgCalculator, SiAtomicConverter

settings.register_profile("ci", deadline=timedelta(seconds=5))
settings.load_profile("ci")


@pytest.fixture(
    scope="session",
    params=[
        "pressure",
        "energy",
        "temperature",
        "volume",
        "entropy",
        "heat_capacity",
        "sound_speed",
    ],
)
def quantity(request):
    yield request.param


@pytest.fixture(scope="session")
def from_si_converter():
    yield SiAtomicConverter(from_si=True)


@pytest.fixture(scope="session")
def to_si_converter():
    yield SiAtomicConverter(from_si=False)


LEFT_LIMIT = 1e-30
RIGHT_LIMIT = 1e20
volumes_st = st_numpy.arrays(
    np.float64,
    st.tuples(st.integers(1, 100)),
    elements=st.floats(LEFT_LIMIT, RIGHT_LIMIT),
)
temperatures_st = st_numpy.arrays(
    np.float64, st.tuples(st.integers(0, 100)), elements=st.floats(1e-49, 1e-30)
)
temperatures_high = st_numpy.arrays(
    np.float64, st.tuples(st.integers(0, 100)), elements=st.floats(1.0e40, 1.0e49)
)


# TODO: tests for various values of g
@contextmanager
def set_up(temps, vols):
    yield (
        IfgCalculator(temperatures=temps, volumes=vols, g=2.0, input_in_si=False),
        np.meshgrid(vols, temps),
    )
