from faker import Faker
import datetime
from collections import Counter
import numpy as np

fake = Faker()



def get_days(count: int) -> list:
    lst = []
    for i in range(count):
        lst.append( fake.date_between(start_date=datetime.date(year=2022, month=1, day=1),
                                    end_date=datetime.date(year=2022, month=12, day=31)) )
    return lst


def first_days(lst: list, count: int, divider=4):
    print(f'\nHere are {count} birthdays:')

    for arr in np.array_split(lst, divider):
        print(*[i.strftime('%b %d') for i in arr], sep=', ')


def check_day(lst: list):

    day, c = Counter(lst).most_common(1)[0]

    if c > 1:
        print(f'\nIn this simulation, {c} people have a birthday on {day.strftime("%b %d")}')
    else:
        print('\nIn this simulation, everyone has his own birthday')


def check_simulations(t: int, count: int) -> int:
    matched = 0
    for i in range(t):
        if i % 10000 == 0:
            print(f'\n{i} simulations run...')
        test = get_days(count)
        _, c = Counter(test).most_common(1)[0]
        if c > 1:
            matched += 1
    return matched


def get_result(m: int, t: int, count: int):

    chance = round( m / t * 100, 2 )

    print(f'\nOut of {t} simulations of {count} people,\n'
          f'there was a matching birthday in that group {m} times.'
          f'\nThis means that {count} people have a {chance}% chance'
          f'\nof having a matching birthday in their group.'
          f'\nThat\'s probably more than you would think!')


def main():
    bdays_count = int(input('How many birthdays shall I generate? (Max: 100) '))
    bdays = get_days(bdays_count)

    first_days(bdays, bdays_count, divider=5)
    check_day(bdays)

    times = int(input('\nHow many simulations shall I run? '))
    matched_bdays = check_simulations(times, bdays_count)
    get_result(matched_bdays, times, bdays_count)


if __name__ == '__main__':
    main()
