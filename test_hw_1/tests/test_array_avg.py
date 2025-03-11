from test_hw_1.Array import Array
import pytest

@pytest.mark.parametrize('data, expected',[
    ((1,2,3),6),
    ((-1,2,3),4),
    ((-1,-2,-3),-6),
    ((-1,-2,3),0)
])

def test_positive(data,expected):
    assert Array(*data).sum() == expected


@pytest.mark.parametrize('data, expected',[
    ((1,-1),0),
    ([0],0)
])

def test_bound(data,expected):
    assert Array(*data).sum() == expected


@pytest.mark.parametrize('data, expected',[
    (('', 1), TypeError),
    ((22, [55]), TypeError),
    (('0', 0), TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        Array(*data).sum()