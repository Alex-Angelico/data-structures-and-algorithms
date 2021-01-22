import pytest
import .multi_bracket_validation.multi_bracket_validation


@pytest.mark.parameterize(
    "test_input_true,expected",
    [
        '{}',
        '{}(){}',
        '()[[Extra Characters]]',
        '(){}[[]]',
        '{}{Code}[Fellows](())',
    ]
)
@pytest.mark.parameterize(
    "test_input_false,expected",
    [
        '[({}]',
        '(](',
        '{(})',
        '{',
        ')',
    ]
)
def test_true(test_input_true, expected):
    actual = multi_bracket_validation(test_input_true)
    assert actual == expected


def test_false(test_input_false, expected):
    actual = multi_bracket_validation(test_input_false)
    assert actual == expected
