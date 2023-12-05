import string
from pprint import pprint


def read_file():
    file = open("test.txt", "r")
    return file


def return_file_as_dict(file):
    dict_of_schematic_lists = {}
    x = 1

    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        line_as_list = list(line)
        dict_of_schematic_lists[x] = line_as_list
        x += 1

    return dict_of_schematic_lists


def get_valid_part_numbers(schematics_dict):
    for line_num, schem_list in schematics_dict.items():
        for item in schem_list:
            print(type(item))
            # if type(item) is string:
            #     print(item + " is string")
            # elif type(item) is int:
            #     print(item + " is int")
            # else:
            #     print("neither")



def solve_part_1():
    file = read_file()
    schematics_dict = return_file_as_dict(file)
    get_valid_part_numbers(schematics_dict)



if __name__ == '__main__':
    solve_part_1()
    # solve_part_2()