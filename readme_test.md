Команда для запуска тестов doctest из консоли для функции encode
(функция test-encode в файле morse-test.py):

python -m doctest -f "путь к файлу morse_test.py" без двойных кавычек

Вывод (пример упавшего теста):
Failed example:
    test_encode('SOS')
Expected:
    '... --- ..'
Got:
    '... --- ...'
**********************************************************************
1 items had failures:
   1 of   1 in morse_test.test_encode
***Test Failed*** 1 failures.
При всех пройденных тестах выведется пустая строка.

Для более полного вывода о тестах используем флаг -v:

python -i "путь к файлу morse_test.py" -v
ИЛИ
через флаг doctest:
python -m doctest -v "путь к файлу morse_test.py"

Вывод (примеры всех пройденных тестов):
Trying:
    test_encode('SOS')
Expecting:
    '... --- ...'
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
2 items had no tests:
    __main__
    __main__.test_decode
1 items passed all tests:
   4 tests in __main__.test_encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.

Вывод (падение теста, вызывающего исключение):
Trying:
    test_encode('SOS')
Expecting:
    '... --- ...'
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
**********************************************************************
File "C:\Users\maxxx\aaa-python-tasks\omd\morse_test.py", line 11, in __main__.test_encode
Failed example:
    test_encode('HELLO = MY NAME IS MAX')
Expected:
    Traceback (most recent call last):
        ...
    KeyError: '='
Got:
    '.... . .-.. .-.. ---   --.----.--.   -- -.--   -. .- -- .   .. ...   -- .- -..-'
Trying:
    test_encode('privet')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 'p'
ok
2 items had no tests:
    __main__
    __main__.test_decode
**********************************************************************
1 items had failures:
   1 of   4 in __main__.test_encode
4 tests in 3 items.
3 passed and 1 failed.
***Test Failed*** 1 failures.

В случае, если нет необходимости контролировать КОЛИЧЕСТВО пробелов, а важно
только их НАЛИЧИЕ, можно произвести тест с помощью флага NORMALIZE_WHITESPACE:

python -m doctest -f "путь до файла morse_test.py" -o NORMALIZE_WHITESPACE -v
Результаты тестов при таком тестировании:

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
2 items had no tests:
    morse_test
    morse_test.test_decode
1 items passed all tests:
   4 tests in morse_test.test_encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.

В случае пробельно зависимого теста необходимо прописать директиву в самом тесте
следующим образом:

# doctest: +(-)option_name, [+(-)option_name, ...]

Отключим пробельную независимость с помощью директивы на одном из тестов:
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
    '         '
ok
2 items had no tests:
    morse_test
    morse_test.test_decode
1 items passed all tests:
   5 tests in morse_test.test_encode
5 tests in 3 items.
5 passed and 0 failed.
Test passed.

C:\Users\maxxx>python -m doctest -f C:\Users\maxxx\aaa-python-tasks\omd\morse_test.py -o NORMALIZE_WHITESPACE -v
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

Для тестирования функции decode в модуле morse_test находится функция test_decode.
Тесты реализованы с помощью библиотеки pytest и включают в себя два верных и два
ошибочных теста. Запуск теста производится с помощью:

pytest "путь до файла morse_test.py"::test_decode

Пример вывода результатов тестирования:
platform win32 -- Python 3.9.7, pytest-7.3.1, pluggy-1.0.0
rootdir: 'имя корневой директории'
plugins: anyio-3.6.2, dash-2.11.0, hypothesis-6.75.3
collected 4 items

'путь к файлу morse_test.py' ..xx                                                                       [100%]

=========================================== 2 passed, 2 xfailed in 0.68s ===========================================


Для тестирования функции one_hot_encoder реализован тест one_hot_encoder_test
с использованием библиотеки unittest; для проведения теста необходимо перейти
в корневую папку проекта, а далее написать следующую команду:

python -m unittest -v one_hot_encoder_test

Результаты срабатывания тестов должны быть следующие:

test_args (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_elememnt_type (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_neg (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_pos (one_hot_encoder_test.OneHotEncoderTest) ... ok
test_transform (one_hot_encoder_test.OneHotEncoderTest) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK

Для запуска дополнительных тестов, реализованных с помощью pytest, необходимо
в консоли ввести команду:

pytest "путь к файлу one_hot_encoder_test.py"

Результаты тестов:
=============================================== test session starts ================================================
platform win32 -- Python 3.9.7, pytest-7.3.1, pluggy-1.0.0
rootdir: C:\Users\maxxx
plugins: anyio-3.6.2, dash-2.11.0, hypothesis-6.75.3
collected 5 items

aaa-python-tasks\omd\one_hot_encoder_test.py .....                                                            [100%]

================================================ 5 passed in 0.05s =================================================

Тестирование функции what_is_year_now (проводим из корневой папки проекта):

pytest what_is_year_now_test.py
(Проводить можно из любого места, но удобнее через рабочую папку, т.к. далее 
проводится тест покрытия; его результаты (директорию с html-файлами) удобнее 
смотреть сразу 'на месте').

Ожидаемый результат:
test_func (what_is_year_now_test.WhatIsYearNowTest)
A decorator for applying a mark on test functions and classes. ... ok

----------------------------------------------------------------------
Ran 1 test in 0.003s

OK

Тест для проверки покрытия кода (запускаем так же из корневой папки проекта):

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
