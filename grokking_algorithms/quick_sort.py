import random


def quick_sort(ex_list: list[int]) -> list[int]:
    if not ex_list:
        return []
    q = ex_list[0]
    less_q = [i for i in ex_list[1:] if q > i]
    more_q = [i for i in ex_list[1:] if q <= i]
    return quick_sort(less_q) + [q] + quick_sort(more_q)


if __name__ == '__main__':
    test_list = [random.randint(1, 100) for _ in range(random.randint(1, 15))]
    print(test_list,
          quick_sort(test_list), sep='\n')
