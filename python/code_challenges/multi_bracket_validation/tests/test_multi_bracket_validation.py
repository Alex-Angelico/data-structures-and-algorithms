import pytest
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


@pytest.mark.parametrize(
    "test_input_true,expected",
    [
        ('{}', True),
        ('{}(){}', True),
        ('()[[Extra Characters]]', True),
        ('(){}[[]]', True),
        ('{}{Code}[Fellows](())', True)
    ]
)
def test_true(test_input_true, expected):
    actual = multi_bracket_validation(test_input_true)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input_false,expected",
    [
        ('[({}]', False),
        ('(](', False),
        ('{(})', False),
        ('{', False),
        (')', False)
    ]
)
def test_false(test_input_false, expected):
    actual = multi_bracket_validation(test_input_false)
    assert actual == expected
