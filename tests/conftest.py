import pytest
from ifg_py import SiAtomicConverter


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
