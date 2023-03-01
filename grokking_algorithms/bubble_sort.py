import random


def bubble_sort(ex_list: list) -> list:
    for iteration in range(1, len_ex_list := len(ex_list)):
        for i in range(len_ex_list - iteration):
            if ex_list[i] > ex_list[i + 1]:
                ex_list[i], ex_list[i + 1] = ex_list[i + 1], ex_list[i]
    return ex_list


if __name__ == '__main__':
    rand_list = [random.randint(1, 100) for _ in range(random.randint(0, 15))]
    print(rand_list)
    print(bubble_sort(rand_list))
