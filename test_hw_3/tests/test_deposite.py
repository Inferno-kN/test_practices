import pytest
from test_hw_3.BankAccount import BankAccount


@pytest.fixture(scope= 'function')
def bank_account():
    return BankAccount()


@pytest.mark.parametrize('input_data, expected',[
    (11,11),
    (100, 100),
    (1234, 1234)
])

def test_positive(bank_account,input_data,expected):
    assert bank_account.deposit(input_data) == expected

@pytest.mark.parametrize('input_data, expected',[
    (0,0)
])

def test_bound(bank_account, input_data,expected):
    assert bank_account.deposit(input_data) == expected

@pytest.mark.parametrize('input_data, expected',[
    (-1, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(bank_account, input_data,expected):
    with pytest.raises(expected):
        bank_account.deposit(input_data)