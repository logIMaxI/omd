import pytest
from what_is_year_now import what_is_year_now
from unittest.mock import patch
from unittest import main


@pytest.mark.parametrize(
    "got, expected",
    [
        ({"currentDateTime": "2023-11-03T14:58Z"}, 2023),
        ({"currentDateTime": "01.02.1998T14:58Z"}, 1998),
        ({"currentDateTime": "02.?1998-?01T12:44Z"}, ValueError),
    ],
)
def test_func(got: dict, expected: int) -> None:
    """
    Function for test func what_is_year_now from according named module
    ------
    :param: got - parameter for testing (example of gotten data)
    :type got: dict

    :param: expected - parameter for testing (expected result of func)
    :type expected: int
    ------
    :raises: AssertionError if func result not equals expected value
    """
    with patch("what_is_year_now.json.load") as mock_load:
        mock_load.return_value = got
        if got == {"currentDateTime": "02.?1998-?01T12:44Z"}:
            with pytest.raises(ValueError):
                what_is_year_now()
        else:
            result = what_is_year_now()
            assert what_is_year_now() == expected


if __name__ == "__main__":  # progma: no cover
    main()
