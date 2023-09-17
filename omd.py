def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    options = {'да': True, 'нет': False}
    print(f'Выберите, пойдёт ли сегодня дождь? {list(options.keys())[0]}/{list(options.keys())[1]}')
    answer = input()
    while answer.lower() not in options.keys():
        print('Неверный ответ. Попробуйте что-то из предложенных: ' +
              f'{list(options.keys())[0]}/{list(options.keys())[1]}')
        answer = input()
    answer = answer.lower()

    if options[answer]:
        print('Уточка-маляр 🦆 счастлива, не осталась без зонта ☂ в плохую погоду! ' +
              'Но уточка устала и решила вернуться домой спать')
    else:
        print('Зонтик ☂ не понадобился, уточка-маляр 🦆 отправилась в бар.')
        drinks = {'А': 'кофе', 'Б': 'сидр', 'В': 'напиток, известный только уткам'}
        print(f'Что же выпить уточке?')
        for action_key, action in drinks.items():
            print(f'{action_key}. {action}')
        answer = input()
        while answer.upper() not in drinks.keys():
            print('Неверный ответ. Попробуйте что-то из предложенных')
            answer = input()
        answer = answer.upper()

        if drinks[answer] == 'кофе':
            print('Уточке 🦆 завтра на работу, поэтому кофе - неплохой вариант')
        elif drinks[answer] == 'сидр':
            print('Завтра уточка 🦆 выходная, поэтому сегодня отдыхаем')
        else:
            print('"Кря-кря, очень вкусный ******" - говорит уточка 🦆')


def step2_no_umbrella():
    options = {'да': True, 'нет': False}
    print(f'Выберите, пойдёт ли сегодня дождь? {list(options.keys())[0]}/{list(options.keys())[1]}')
    answer = input()
    while answer.lower() not in options.keys():
        print('Неверный ответ. Попробуйте что-то из предложенных:' +
              f'{list(options.keys())[0]}/{list(options.keys())[1]}')
        answer = input()
    answer = answer.lower()

    if options[answer]:
        print('О нет! Пошёл дождь, а у уточки 🦆 нет зонтика ☂! Что же делать?')
        options = {'А': 'вернуться домой и отдыхать', 'Б': 'бежать в бар', 'В': 'погрустить в парке на лавочке'}
        for action_key, action in options.items():
            print(f'{action_key}. {action}')
        answer = input()
        while answer.upper() not in options.keys():
            print('Неверный ответ. Попробуйте что-то из предложенных')
            answer = input()
        answer = answer.upper()

        if options[answer] == 'вернуться домой и отдыхать':
            print('Уточка 🦆 расстроилась из-за дождя, устала и пошла отдыхать домой.')
        elif options[answer] == 'бежать в бар':
            print('Уточка 🦆 влетела в бар, испугав барменов. Уточка 🦆 не ознакомилась с ' +
                  'меню, но бармены так напуганы, что приготвят любой напиток, что вы закажете.')
            print('Что же выпить уточке 🦆 в баре?')
            answer = input()
            print(f'Ей приготовили {answer}. Она довольна.')
        else:
            print('Уточка пошла грустить на лавочке в парке...')
            print(':(')
            print('Но тут уточка 🦆 увидела другую уточку 🦆, у которой бвл зонтик. +1 друг, ура!')

    else:
        print('Уточке 🦆 не взяла зонтик ☂, но дождя не было - вот это удача! Надо это отпраздновать!')
        drinks = {'А': 'кофе', 'Б': 'сидр', 'В': 'напиток, известный только уткам'}
        print(f'Что же выпить уточке в баре?')
        for action_key, action in drinks.items():
            print(f'{action_key}. {action}')
        answer = input()
        while answer.upper() not in drinks.keys():
            print('Неверный ответ. Попробуйте что-то из предложенных')
            answer = input()
        answer = answer.upper()

        if drinks[answer] == 'кофе':
            print('Уточке 🦆 завтра на работу, поэтому кофе - неплохой вариант')
        elif drinks[answer] == 'сидр':
            print('Завтра уточка 🦆 выходная, поэтому сегодня отдыхаем')
        else:
            print('"Кря-кря, очень вкусный ******" - говорит уточка 🦆')


if __name__ == '__main__':
    step1()
