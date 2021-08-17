import pytest

from ifg import IfgCalculator


@pytest.fixture(params=["P", "S", "E", "mu", "C_P", "C_V", "C_T", "C_S"])
def attribute(request):
    yield request.param


def test_has_attribute(attribute):
    assert hasattr(IfgCalculator, attribute)


def test_cannot_skip_temperature_definition(attribute):
    # GIVEN: calculator without temperatures set
    # WHEN: any attribute of IFG is accessed
    # THEN: ValueError with proper text is called
    with pytest.raises(ValueError) as e:
        calculator = IfgCalculator(volumes=[10.0])
        _ = getattr(calculator, attribute)
        # assert e.value == "temperatures is not set"


def test_cannot_skip_volume_definition(attribute):
    # GIVEN: calculator without volumes set
    # WHEN: any attribute of IFG is accessed
    # THEN: ValueError with proper text is called
    with pytest.raises(ValueError) as e:
        calculator = IfgCalculator(temperatures=[10.0])
        _ = getattr(calculator, attribute)
        # assert e.value == "volumes is not set"
