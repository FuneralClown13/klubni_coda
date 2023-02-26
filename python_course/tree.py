#!/bin/python3

import os
import os.path

count_dir, count_files = 0, 0


def buildTree(level=0, print_pattern=(0,)):
    global count_dir, count_files

    path = os.getcwd()
    list_directory = sorted(os.listdir(path=path))
    for i, file in enumerate(list_directory):
        last_file = len(list_directory) - i - 1
        if os.path.isdir(f'{path}/{file}'):
            printTreeLine(last_file, print_pattern, file)
            os.chdir(f'{path}/{file}')
            count_dir += 1
            buildTree(level + 1, (*print_pattern, (1 if last_file else 0)))
        else:
            printTreeLine(last_file, print_pattern, file)
            count_files += 1


def printTreeLine(last_file: int, print_pattern: tuple, file_name: str) -> None:
    p_dict = ['    ', '│   ']
    [print(p_dict[key], end='') for key in print_pattern]
    print(('├── ' if last_file else '└── ') + file_name)

def test(path: str):
    os.chdir(path)
    buildTree()

if __name__ == '__main__':
    #test('/home/funeralclown/testtree')
    buildTree()
    print(f'{count_dir} directories, {count_files} files')
