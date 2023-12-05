def strip_non_digits(line):
    digits_string = ''.join([i for i in line if i.isdigit()])
    return digits_string


def find_string_digits(line):
    digits_as_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    x = 0
    while x < len(digits_as_strings):
        num = digits_as_strings[x]
        if num in line:
            line = line.replace(str(num), str(num) + str(x + 1) + str(num))
        x += 1
    return line


def solve_part_1():
    ints = 0

    file = read_file()

    for line in file:
        digits_string = strip_non_digits(line)
        new_int = int(digits_string[0] + digits_string[-1])
        ints += new_int

    print("Part 1 = " + str(ints))


def solve_part_2():
    ints = 0

    file = read_file()

    for line in file:
        line = find_string_digits(line)
        digits_string = strip_non_digits(line)
        new_int = int(digits_string[0] + digits_string[-1])
        ints += new_int

    print("Part 2 = " + str(ints))


def read_file():
    file = open("1/input.txt", "r")
    return file


if __name__ == '__main__':
    solve_part_1()
    solve_part_2()

