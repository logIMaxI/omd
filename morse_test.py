import morse
import doctest
import pytest


def test_encode(message: str) -> str:
    """
    Function for testing encode function from morse.py module
    ------
    :param: message - string to encode
    :type message: str
    ------
    :rtype: str
    :return: encoded string
    ------

    >>> test_encode('SOS')
    '... ---       ...'
    >>> test_encode('HELLO MY NAME IS MAX')
    '.... . .-.. .-.. ---   -- -.--   -. .- -- .   .. ...   -- .- -..-'
    >>> test_encode('HELLO = MY NAME IS MAX')
    Traceback (most recent call last):
        ...
    KeyError: '='
    >>> test_encode('privet')
    Traceback (most recent call last):
        ...
    KeyError: 'p'
    >>> test_encode('     ') # doctest: -NORMALIZE_WHITESPACE
    '         '
    """
    return morse.encode(message)


@pytest.mark.parametrize(
    'message, expected',
    [
        ('.... . .-.. .-.. ---', 'HELLO'),
        (
                '.- ...- .. - --- -....- .- -. .- .-.. -.-- ... '
                '- ... -....- .- -.-. .- -.. . -- -.--',
                'AVITO-ANALYSTS-ACADEMY',
        ),
        pytest.param(
            '.. -....- .- -- -....- -- .- -.. -.. -...',
            'I-AM-MAX',
            marks=pytest.mark.xfail,
        ),
        pytest.param(
            '..-. .-. ..- .. --- -- -....- -- --- ... -.-. --- .--',
            'FROM-MOSCOW',
            marks=pytest.mark.xfail,
        ),
    ],
)
def test_decode(message: str, expected) -> str:
    """
    Function for testing decode function from morse.py module
    ------
    :param: message - string to decode
    :type message: str
    ------
    :raises: AssertionError if decoded string doesn't equal expected result
    ------
    :rtype: str
    :return: decoded string
    ------
    """
    assert morse.decode(message) == expected


if __name__ == "__main__":
    doctest.testmod()
