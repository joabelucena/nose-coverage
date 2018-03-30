from nose.tools import assert_equal
from mymath.basic_operations import subtract

def test_subtract():
    assert_equal(subtract(3, 2), 1)