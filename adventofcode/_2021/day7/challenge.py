from statistics import median

from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day7/input.txt')
    split_data = [int(crab) for crab in data[0].split(',')]

    best_number = find_median(split_data)
    answer_1 = calculate_fuel(split_data, best_number)

    print(answer_1)

    return answer_1


def find_median(data) -> int:
    median_number = int(median(data))

    return median_number


def calculate_fuel(data, best_number: int):
    """Found out later that Python has `abs()` to get the absolute value so no
    need for the less than or greater than bit which would simplify this a lot.
    """
    total_fuel = 0
    for crab_position in data:
        if crab_position > best_number:
            fuel = crab_position - best_number
            print(fuel)
        elif crab_position < best_number:
            fuel = best_number - crab_position
            print(fuel)
        elif crab_position == best_number:
            fuel = 0

        total_fuel += fuel

    print(total_fuel)

    return total_fuel


if __name__ == '__main__':
    main()
