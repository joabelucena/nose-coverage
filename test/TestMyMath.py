from nose.tools import assert_almost_equal
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises

from mymath.basic_operations import add
from mymath.basic_operations import multiply
from mymath.basic_operations import divide
from mymath.basic_operations import subtract

from nose.tools import assert_raises

def test_add():
    assert_equal(add(1,2), 3)
    assert_not_equal(add(2, 2), 5)
    assert_raises(TypeError, add, 2, "0")

#def test_subtract():
#    assert_equal(subtract(3, 2), 1)


