from test_hw_2.BankAccount import BankAccount
import pytest

@pytest.mark.parametrize('input_data, expected',[
    (11,89),
    (2,98)
])

def test_positive(input_data,expected):
    assert BankAccount.get_balance(input_data) == expected


@pytest.mark.parametrize('input_data, expected',[
    (0,100),
    (100,0),
    (99,1),
    (1,99),
    (-1,101)
])

def test_bound(input_data,expected):
    assert BankAccount.get_balance(input_data) == expected


@pytest.mark.parametrize('input_data, expected',[
    (101, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        BankAccount.get_balance(input_data)