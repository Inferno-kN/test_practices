from test_hw_2.avg import average
import pytest

@pytest.mark.parametrize('data, expected',[
    ([1,2,3],2),
    ([3, 4, 5],4),
    ([2, 2], 2),
])

def test_positive(data,expected):
    assert average(data) == expected


@pytest.mark.parametrize('data, expected',[
    ([1],1),
    ([0],0)
])

def test_bound(data,expected):
    assert average(data) == expected


@pytest.mark.parametrize('data, expected',[
    (3.14, TypeError),
    (None, ValueError),
    ([], ValueError),
    ([''], TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        average(data)