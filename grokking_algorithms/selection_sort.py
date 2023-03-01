import random


def selection_sort(ex_list: list) -> list:
    sorted_list = []
    for num in range(len(ex_list)):
        sorted_list.append(ex_list.pop(find_smallest(ex_list)))
    return sorted_list


def find_smallest(ex_list: list) -> int:
    smallest, smallest_i = ex_list[0], 0
    [[smallest := num, smallest_i := i] for i, num in enumerate(ex_list) if num < smallest]
    return smallest_i


if __name__ == '__main__':
    rand_list = [random.randint(1, 100) for _ in range(random.randint(0, 15))]
    print(rand_list)
    print(selection_sort(rand_list))
