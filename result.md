## Тесты для первого задания

**python -m doctest -f C:\Users\maxxx\aaa-python-tasks\omd\morse_test.py -o NORMALIZE_WHITESPACE -v**

Trying:
    test_encode('SOS')
Expecting:
    '... ---       ...'
ok
Trying:
    test_encode('HELLO MY NAME IS MAX')
Expecting:
    '.... . .-.. .-.. ---   -- -.--   -. .- -- .   .. ...   -- .- -..-'
ok
Trying:
    test_encode('HELLO = MY NAME IS MAX')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: '='
ok
Trying:
    test_encode('privet')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 'p'
ok
Trying:
    test_encode('     ') # doctest: -NORMALIZE_WHITESPACE
Expecting:
    '          '
**********************************************************************
File "C:\Users\maxxx\aaa-python-tasks\omd\morse_test.py", line 19, in morse_test.test_encode
Failed example:
    test_encode('     ') # doctest: -NORMALIZE_WHITESPACE
Expected:
    '          '
Got:
    '         '
2 items had no tests:
    morse_test
    morse_test.test_decode
**********************************************************************
1 items had failures:
   1 of   5 in morse_test.test_encode
5 tests in 3 items.
4 passed and 1 failed.
***Test Failed*** 1 failures.
---

## Тесты для второго задания
**pytest "путь до файла morse_test.py"::test_decode**

Пример вывода результатов тестирования:

platform win32 -- Python 3.9.7, pytest-7.3.1, pluggy-1.0.0
rootdir: 'имя корневой директории'
plugins: anyio-3.6.2, dash-2.11.0, hypothesis-6.75.3
collected 4 items

'путь к файлу morse_test.py' ..xx                                                                       [100%]

=========================================== 2 passed, 2 xfailed in 0.68s ===========================================
---

## Тесты для третьего задания

**python -m unittest -v one_hot_encoder_test**

Результаты срабатывания тестов должны быть следующие:

test_args (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_elememnt_type (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_neg (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_pos (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_transform (one_hot_encoder_test.OneHotEncoderTest) ... ok

Ran 5 tests in 0.005s

OK
---

## Тесты для четвёртого задания

**pytest "путь к файлу one_hot_encoder_test.py"**

Результаты тестов:
=============================================== test session starts ================================================
platform win32 -- Python 3.9.7, pytest-7.3.1, pluggy-1.0.0
rootdir: C:\Users\maxxx
plugins: anyio-3.6.2, dash-2.11.0, hypothesis-6.75.3
collected 5 items

aaa-python-tasks\omd\one_hot_encoder_test.py .....                                                            [100%]

================================================ 5 passed in 0.05s =================================================
---

## Тесты для пятого задания

**pytest what_is_year_now_test.py**

Ожидаемый результат:

test_func (what_is_year_now_test.WhatIsYearNowTest)
A decorator for applying a mark on test functions and classes. ... ok

Ran 1 test in 0.003s

OK

pytest what_is_year_now_test.py --cov --cov-report=html

Ожидаемый вывод:

platform win32 -- Python 3.9.7, pytest-7.3.1, pluggy-1.0.0
rootdir: C:\Users\maxxx\aaa-python-tasks\omd
plugins: anyio-3.6.2, dash-2.11.0, hypothesis-6.75.3, cov-4.1.0
collected 3 items

what_is_year_now_test.py ...                                                                                     [100%]

----------- coverage: platform win32, python 3.9.7-final-0 -----------
Coverage HTML written to dir htmlcov


================================================== 3 passed in 8.26s ==================================================

При этом в директории htmlcov текущего проекта в файле what_is_year_now_py.html 
содержатся результаты теста с процентом покрытия.
