from utils import division
import pytest
from utils import func

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (4, 2, 2),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_excepion, divider, divisionable",
                         [(ZeroDivisionError, 0, 10),
                          (TypeError, '2', 20)])
def test_division_with_error(expected_excepion, divider, divisionable):
    with pytest.raises(expected_excepion):
        division(divisionable, divider)

def test_system_exit():
    with pytest.raises(SystemExit):
        func()

