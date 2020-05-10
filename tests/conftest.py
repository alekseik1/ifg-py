from contextlib import contextmanager

import numpy as np
import pytest
from hypothesis import strategies as st
from hypothesis.extra import numpy as st_numpy

from ifg_py import SiAtomicConverter, IfgCalculator


@pytest.fixture(scope='session', params=[
    'pressure', 'energy', 'temperature', 'volume',
    'entropy', 'heat_capacity', 'sound_speed'
])
def quantity(request):
    yield request.param


@pytest.fixture(scope='session')
def from_si_converter():
    yield SiAtomicConverter(from_si=True)


@pytest.fixture(scope='session')
def to_si_converter():
    yield SiAtomicConverter(from_si=False)


volumes_st = st_numpy.arrays(np.float, st.tuples(st.integers(1, 1)),
                             elements=st.floats(10., 100.))
temperatures_st = st_numpy.arrays(np.float, st.tuples(st.integers(0, 100)),
                                  elements=st.floats(1E-49, 1E-30))
temperatures_high = st_numpy.arrays(np.float, st.tuples(st.integers(0, 100)),
                                    elements=st.floats(1.E+40, 1.E+49))


@contextmanager
def set_up(temps, vols):
    yield (IfgCalculator(
        temperatures=temps, specific_volumes=vols,
        input_in_si=False, output_in_si=False), np.meshgrid(vols, temps))
