from hypothesis import strategies as st, given
from pytest import approx


allowed_numbers = st.floats(min_value=1e-50, max_value=1e+50)
# One in atomic is `atomic_to_si[quantity]` in SI
atomic_to_si = {
    'pressure': 29421015696686.086,
    'energy': 4.3597447222071E-18,
    'temperature': 315775.02480232634,
    'volume': 1.481847114721628e-31,
    'entropy': 1.380649E-23,
    'heat_capacity': 1.380649E-23,
    'sound_speed': 2187691.2636411325,
}


@given(allowed_numbers)
def test_to_and_back_are_equal(quantity, from_si_converter, to_si_converter, value):
    converted = getattr(from_si_converter, 'convert_{}'.format(quantity))(value)
    original = getattr(to_si_converter, 'convert_{}'.format(quantity))(converted)
    assert value == approx(original)


@given(allowed_numbers)
def test_correct_from_atomic(quantity, to_si_converter, value):
    converted = getattr(to_si_converter, 'convert_{}'.format(quantity))(value)
    assert converted == approx(value*atomic_to_si[quantity])


@given(allowed_numbers)
def test_correct_from_si(quantity, from_si_converter, value):
    converted = getattr(from_si_converter, 'convert_{}'.format(quantity))(value)
    assert converted == approx(value/atomic_to_si[quantity])
