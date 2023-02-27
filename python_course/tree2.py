#!/bin/python3

import os
import os.path

count_dir, count_files = 0, 0


def start_end_output():
    print('.')
    build_tree()
    print(f'\n{count_dir} directories, {count_files} files')


def build_tree(level=0, print_pattern='') -> None:
    path = os.getcwd()
    list_directory, len_list_directory = get_directory(path)

    for i, file in enumerate(list_directory):
        print_tree_line(last_file_flag := len_list_directory - i - 1, print_pattern, file)

        if is_dir := os.path.isdir(new_path := f'{path}/{file}'):
            os.chdir(new_path)
            build_tree(level + 1, (print_pattern + ('│   ' if last_file_flag else '    ')))

        counter(is_dir)


def get_directory(path: str) -> tuple:
    list_directory = sorted(os.listdir(path=path))
    len_list_directory = len(list_directory)
    return list_directory, len_list_directory


def print_tree_line(last_file: int, print_pattern: str, file_name: str):
    print(print_pattern + ('├── ' if last_file else '└── ') + file_name)


def counter(is_dir: bool):
    global count_dir, count_files

    if is_dir:
        count_dir += 1
    else:
        count_files += 1


if __name__ == '__main__':
    start_end_output()

"""
    def test(path: str):
        os.chdir(path)
        start_end_output()


    test('/home/funeralclown/testtree')
    test('/home/funeralclown/klubni_coda')
    test('/home/funeralclown/slunix_course')"""
