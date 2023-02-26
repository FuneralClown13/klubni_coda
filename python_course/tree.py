#!/bin/python3

import os
import os.path

count_dir, count_files = 0, 0


def build_tree(level=0, print_pattern=(0,)) -> None:
    global count_dir, count_files

    path = os.getcwd()
    list_directory = sorted(os.listdir(path=path))
    for i, file in enumerate(list_directory):
        last_file_flag = len(list_directory) - i - 1
        if os.path.isdir(f'{path}/{file}'):
            print_tree_line(last_file_flag, print_pattern, file)
            count_dir += 1
            os.chdir(f'{path}/{file}')
            build_tree(level + 1, (*print_pattern, (1 if last_file_flag else 0)))
        else:
            print_tree_line(last_file_flag, print_pattern, file)
            count_files += 1


def print_tree_line(last_file: int, print_pattern: tuple, file_name: str) -> None:
    p_dict = ['    ', '│   ']
    [print(p_dict[key], end='') for key in print_pattern[1:]]
    print(('├── ' if last_file else '└── ') + file_name)


if __name__ == '__main__':
    print('.')
    build_tree()
    print(f'\n{count_dir} directories, {count_files} files')


    def test(path: str):
        os.chdir(path)
        build_tree()

    # test('/home/funeralclown/testtree')
