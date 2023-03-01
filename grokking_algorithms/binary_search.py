def binary_search(ex_list: list[int], goal: int) -> str:
    while ex_list[1:]:
        if ex_list[q := len(ex_list) // 2] == goal:
            return f'{goal} was found'
        ex_list[:] = ex_list[:q] if ex_list[q] > goal else ex_list[q:]
    return f'{goal} is not in the list'


if __name__ == '__main__':
    test_list = list(range(16))
    search_value = 12
    print(binary_search(test_list, search_value))
