from collections import Counter
from statistics import median

from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day7/sample.txt')
    answer_1 = some_function(data)
    # answer_2 = some_function(data)

    print(answer_1, answer_2)

    return answer_1, answer_2


def some_function(data):
    split_data = [int(crab) for crab in data[0].split(',')]
    median_number = int(median(split_data))
    # print(median_number)

    total_fuel = 0
    for crab_position in split_data:
        if crab_position > median_number:
            fuel = crab_position - median_number
            print(fuel)
        elif crab_position < median_number:
            fuel = median_number - crab_position
            print(fuel)
        elif crab_position == median_number:
            fuel = 0

        total_fuel += fuel

    print(total_fuel)


if __name__ == '__main__':
    main()
