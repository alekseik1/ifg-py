from ifg.calculator import THRESHOLD
from hypothesis import strategies as st, given
from tests.conftest import volumes_st, set_up
import numpy as np
import hypothesis.extra.numpy as st_numpy

temps_left_st = st_numpy.arrays(np.float, (100, ), elements=st.floats(
    THRESHOLD*(1-1e-7), THRESHOLD, exclude_max=True))
temps_right_st = st_numpy.arrays(np.float, (100, ), elements=st.floats(
    THRESHOLD, THRESHOLD*(1+1e-7), exclude_min=True))


@given(temps_left_st, temps_right_st, volumes_st)
def test_left_right_limits_are_equal(temps_left, temps_right, vols):
    with set_up(temps_left, vols) as (calc1, (vv, tt)):
        left_C_V = calc1.C_V
        left_C_P = calc1.C_P
        left_entropy = calc1.S
    with set_up(temps_right, vols) as (calc2, (vv, tt)):
        right_C_V = calc2.C_V
        right_C_P = calc2.C_P
        right_entropy = calc2.S
    np.testing.assert_allclose(left_C_V, right_C_V)
    np.testing.assert_allclose(left_C_P, right_C_P)
    np.testing.assert_allclose(left_entropy, right_entropy)
