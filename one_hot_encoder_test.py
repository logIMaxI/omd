from unittest import TestCase, main
from one_hot_encoder import fit_transform
import pytest


class OneHotEncoderTest(TestCase):
    """
    Class for testing one_hot_encoder func from according named module
    ------
    :method: test_pos - positive tests
    :method: test_neg - negative tests
    :method: test_transform - one more positive test
    :method: test_element_type - test for checking rtype correct
    :method: test_args - exception test
    """

    def test_pos(self: OneHotEncoderTest) -> None:
        """
        Method for positive tests
        ------
        :param: self - reference to object of current class
        :type self: OneHotEncoderTest
        """
        self.assertEqual(
            [
                ("Moscow", [0, 0, 1]),
                ("SPB", [0, 1, 0]),
                ("Regions", [1, 0, 0])
            ],
            fit_transform(["Moscow", "SPB", "Regions"]),
        )
        self.assertEqual(
            [
                ("A", [0, 0, 0, 0, 1]),
                ("A", [0, 0, 0, 0, 1]),
                ("B", [0, 0, 0, 1, 0]),
                ("C", [0, 0, 1, 0, 0]),
                ("D", [0, 1, 0, 0, 0]),
                ("B", [0, 0, 0, 1, 0]),
                ("E", [1, 0, 0, 0, 0]),
            ],
            fit_transform(["A", "A", "B", "C", "D", "B", "E"]),
        )

    def test_neg(self):
        """
        Method for negative tests
        ------
        :param: self - reference to object of current class
        :type self: OneHotEncoderTest
        """
        self.assertNotEqual(
            [
                ("Moscow", [1, 0, 0]),
                ("SPB", [0, 1, 0]),
                ("Regions", [0, 0, 1])
            ],
            fit_transform(["Moscow", "SPB", "Regions"]),
        )
        self.assertNotEqual(
            [
                ("A", [0, 0, 0, 0, 1]),
                ("A", [0, 0, 0, 0, 1]),
                ("B", [0, 0, 0, 0, 1]),
                ("C", [0, 0, 1, 0, 0]),
                ("D", [0, 1, 0, 0, 0]),
                ("B", [0, 0, 0, 0, 1]),
                ("E", [1, 0, 0, 0, 0]),
            ],
            fit_transform(["A", "A", "B", "C", "D", "B", "E"]),
        )

    def test_transform(self):
        """
        Method for positive test
        ------
        :param: self - reference to object of current class
        :type self: OneHotEncoderTest
        """
        self.assertEqual(
            [
                ("Male", [0, 0, 1]),
                ("Female", [0, 1, 0]),
                ("Not known", [1, 0, 0]),
                ("Female", [0, 1, 0]),
            ],
            fit_transform(["Male", "Female", "Not known", "Female"]),
        )

    def test_elememnt_type(self):
        """
        Method for checking type of returned elements
        ------
        :param: self - reference to object of current class
        :type self: OneHotEncoderTest
        """
        self.assertIsInstance(fit_transform(["A", "B"])[0], tuple)

    def test_args(self):
        """
        Method for exception test
        ------
        :param: self - reference to object of current class
        :type self: OneHotEncoderTest
        """
        with self.assertRaises(TypeError) as er:
            fit_transform()
        self.assertEqual(
            "expected at least 1 arguments, got 0",
            er.exception.args[0]
        )


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            ("A", "B", "A", "C", "A"),
            [
                ("A", [0, 0, 1]),
                ("B", [0, 1, 0]),
                ("A", [0, 0, 1]),
                ("C", [1, 0, 0]),
                ("A", [0, 0, 1]),
            ],
        ),
        (
            ("Male", "Female", "Male"),
            [("Male", [0, 1]), ("Female", [1, 0]), ("Male", [0, 1])],
        ),
        (("Yes", "No"), [("Yes", [0, 1]), ("No", [1, 0])]),
        (
            (1, 2, 4, 2, 5),
            [
                (1, [0, 0, 0, 1]),
                (2, [0, 0, 1, 0]),
                (4, [0, 1, 0, 0]),
                (2, [0, 0, 1, 0]),
                (5, [1, 0, 0, 0]),
            ],
        ),
    ],
)
def pytest_fit_transform(args: tuple, expected: list[tuple]):
    """
    Function for positive tests for function fit_transform in module
    one_hot_encoder.py
    ------
    :param: args - tuple of coding values
    :type args: tuple

    :param: expected - expected result of one-hot-encoding transform
    :type expected: list[tuple]
    ------
    :raises: AssertionError if function result doesn't equal expected result
    """
    assert one_hot_encoder.fit_transform(args) == expected


def pytest_except():
    """
    Function for exception test
    """
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()


if __name__ == "__main__":
    main()
