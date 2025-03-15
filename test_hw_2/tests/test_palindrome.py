from test_hw_2.palindrome import is_palindrome
import pytest

@pytest.mark.parametrize('data, expected',[
    ('111',True),
    ('987',False),
    ('123454321', True),
    ('123567', False)
])

def test_positive(data,expected):
    assert is_palindrome(data) == expected


@pytest.mark.parametrize('data, expected',[
    ('',False),
    ('Txt', False)
])

def test_bound(data,expected):
    assert is_palindrome(data) == expected


@pytest.mark.parametrize('data, expected',[
    (6, TypeError),
    (None, TypeError),
    ([234], TypeError),
    ([], TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        is_palindrome(data)