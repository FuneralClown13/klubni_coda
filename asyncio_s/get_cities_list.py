import re


def get_cities_list() -> list:
    cities = []
    with open('cities.txt', 'r') as cities_txt:
        for line in cities_txt.readlines():
            cities.append(line.strip())
    print('get_cities_list')
    return cities


def set_city_in_list(city):
    with open('cities.txt', 'a+') as cities_txt:
        cities_txt.write(city + '\n')


def del_city_if_404(city):
    print('try del')
    pattern = re.compile(re.escape(city))
    with open('cities.txt', 'r+') as cities_txt:
        lines = cities_txt.readlines()
        cities_txt.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                cities_txt.write(line)
            cities_txt.truncate()
