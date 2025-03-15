from test_hw_2.BankAccount import BankAccount
import pytest

@pytest.mark.parametrize('input_data, expected',[
    (11,11),
    (14,14),
    (100, 100)
])

def test_positive(input_data,expected):
    assert BankAccount.deposit(input_data) == expected


@pytest.mark.parametrize('input_data, expected',[
    (0,0)
])

def test_bound(input_data,expected):
    assert BankAccount.deposit(input_data) == expected

@pytest.mark.parametrize('input_data, expected',[
    (-1, ValueError),
    ('3.13', TypeError),
    ([], TypeError)
])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        BankAccount.deposit(input_data)