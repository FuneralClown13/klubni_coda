import random


def get_rand_list() -> list[int]:
    return [random.randint(1, 20) for _ in range(random.randint(10, 15))]


def test(f, *args, random_values=True, repeat=1, sort=False, test_list=None):
    for _ in range(repeat):
        if random_values:
            rand_list = get_rand_list()
        else:
            rand_list = test_list
        if sort:
            rand_list = sorted(rand_list)
        print(rand_list)
        print(f(rand_list, *args))
