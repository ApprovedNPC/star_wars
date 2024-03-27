import requests
from pprint import pprint

base = 'https://swapi.dev/api/'


def json_from_request(base, endpoint, path='', query=''):
    request = f'{base}{endpoint}{path}{query}'
    # print(request)
    response = requests.get(request)
    data = response.json().get('results')
    # pprint(data) # in reality it is a string formatted in specific way
    return data


def get_all_starships():
    endpoint = 'starships/'
    ship_info = json_from_request(base, endpoint)
    print('All the ships with a hyperdrive rating above 3 are: ')
    for ship in ship_info:
        hyperdrive_rating = float(ship.get('hyperdrive_rating'))

        if hyperdrive_rating > 3:
            print(ship.get('name'))
    print('')
    print('All the ships with cargo capacity above 300000 are: ')

    for ship in ship_info:
        cargo_capacity = float(ship.get('cargo_capacity'))
        if cargo_capacity > 300000:
            print(ship.get('name'))
    print('')
    print('All ships with consumables above 5 months are: ')

    for ship in ship_info:
        duration_consumables = ship.get('consumables').split()
        # print(duration_consumables[1])
        if duration_consumables[1] == 'months':
            int_duration = int(duration_consumables[0])
        if duration_consumables[1] == 'year':
            int_duration = int(duration_consumables[0]) * 12
        # print(int_duration)
        if int_duration > 5:
            print(ship.get('name'))
    print('')
    print('All ships with passengers 0 are: ')
    for ship in ship_info:
        passengers = ship.get('passengers')
        if passengers == str(0):
            print(ship.get('name'))
    print('')


def get_ship_films():
    endpoint = 'starships/'
    ship_info = json_from_request(base, endpoint)
    for ship in ship_info:
        films = ship.get('films')
        print(f"{ship.get('name')} can be found in these films: ")
        endpoint = ''
        print('')


film_title = []


def get_all_films():
    endpoint = 'films/'
    film_names = json_from_request(base, endpoint)

    for film in film_names:
        film_title.append(film.get('title'))
    for i in range(1, len(film_title) + 1):
        print(f'{i}: {film_title[i - 1]}')


def json_from_request():
    request = f'https://swapi.dev/api/people/1/'
    # print(request)
    response = requests.get(request)
    data = response.json().get('results')
    # pprint(data) # in reality it is a string formatted in specific way
    print(data)


json_from_request()
get_all_starships()
print('Welcome to the Star Wars virtual environment.')
get_all_films()
nums = int(input('Which movie would you like to be a part of? (Choose from the following numbers) '))
title = film_title[nums - 1]
print(title)