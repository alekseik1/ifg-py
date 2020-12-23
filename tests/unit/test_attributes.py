import pytest
from ifg import IfgCalculator


@pytest.mark.parametrize('attribute', [
    'P', 'S', 'E', 'mu', 'C_P', 'C_V', 'C_T', 'C_S'
])
def test_has_attribute(attribute):
    assert hasattr(IfgCalculator, attribute)
