import pytest
from test_hw_3.BankAccount import BankAccount

@pytest.fixture(scope= 'function')
def bank_account():
    return BankAccount()


@pytest.mark.ba
@pytest.mark.parametrize('input_data, expected',[
    (11,89),
    (11.1,88.9),
    (2,98),
    (1, 99)
])

def test_positive(bank_account,input_data,expected):
    assert bank_account.withdraw(input_data) == expected


@pytest.mark.ba
@pytest.mark.parametrize('input_data, expected',[
    (100,0),
    (99,1),
    (1,99),
])

def test_bound(bank_account, input_data,expected):
    assert bank_account.withdraw(input_data) == expected


@pytest.mark.ba
@pytest.mark.parametrize('input_data, expected',[
    (101, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(bank_account, input_data,expected):
    with pytest.raises(expected):
        bank_account.withdraw(input_data)