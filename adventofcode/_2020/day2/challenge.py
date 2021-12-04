import re

from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2020/day2/input.txt')
    answer_1, answer_2 = iterate_password_data(data)

    print('Number of valid passwords part 1:', answer_1)
    print('Number of valid passwords part 2:', answer_2)

    return answer_1, answer_2


def iterate_password_data(data):
    re_match = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w+): (?P<password>.+)')
    valid_password_count_1 = 0
    valid_password_count_2 = 0

    for line in data:
        regex_line = re_match.search(line.strip())
        minimum = int(regex_line['min'])
        maximum = int(regex_line['max'])
        letter = regex_line['letter']
        password = regex_line['password']
        if check_valid_password_1(minimum, maximum, letter, password):
            valid_password_count_1 += 1
        if check_valid_password_2(minimum, maximum, letter, password):
            valid_password_count_2 += 1

    return valid_password_count_1, valid_password_count_2


def check_valid_password_1(minimum, maximum, letter, password):
    """PART ONE

    Checks if a password is valid based on the criteria.
    The letter must exist in the password between the min and
    max number of times to be valid.
    """
    if password.count(letter) >= minimum and password.count(letter) <= maximum:
        # print(minimum, maximum, letter, password)
        return True


def check_valid_password_2(minimum, maximum, letter, password):
    """PART TWO

    Checks if a password is valid based on the criteria.
    The min/max in this example are actually the indexes
    (no index 0 here) of where the letter should occur.
    Only one occurence of the letter is acceptable (an "a")
    at both 1 and 3 won't work.
    """
    if (
        password[minimum - 1] == letter
        and password[maximum - 1] != letter
        or password[maximum - 1] == letter
        and password[minimum - 1] != letter
    ):
        # print(minimum, maximum, letter, password)
        return True


if __name__ == '__main__':
    main()
