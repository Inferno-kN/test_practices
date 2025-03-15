import os
import pytest
from test_hw_3.Logger import Logger


@pytest.fixture(scope= 'function')
def logger():
    path_to_test_file = 'test_log.txt'
    logger = Logger(path_to_test_file)

    yield logger

    os.remove(path_to_test_file)


@pytest.mark.parametrize('input_data, expected',[
    ('Кара','Кара')
])

def test_positive(logger, input_data,expected):
    logger.log(input_data)
    assert logger.get_logs()[0].replace('\n', '') == expected


@pytest.mark.parametrize('input_data, expected',[
    (-1, TypeError),
    (3.13, TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(logger, input_data,expected):
    with pytest.raises(expected):
        logger.log(input_data)
        logger.get_logs()[0].replace('\n', '')