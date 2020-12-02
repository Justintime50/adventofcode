from adventofcode.static_data import (
    DAY1_INPUT
)


# TODO: Have a single function that can take an argument for how many numbers to sum

def sum_two_numbers():
    """PART ONE

    Sum all numbers from the DAY1_INPUT list together
    in pairs of num + num until you find two that
    equal 2020.
    """
    num_to_equal = 2020
    for num_1 in DAY1_INPUT:
        for num_2 in DAY1_INPUT:
            sum_total = num_1 + num_2
            if sum_total == num_to_equal:
                print(f'{num_1} + {num_2} = {sum_total}')
                print(f'{num_1} * {num_2} = {num_1 * num_2}')
                return
    print(f'No numbers sum together to equal {num_to_equal}')


def sum_three_numbers():
    """PART TWO

    Sum all numbers from the DAY1_INPUT list together
    in sets of num + num + num until you find two that
    equal 2020.
    """
    num_to_equal = 2020
    for num_1 in DAY1_INPUT:
        for num_2 in DAY1_INPUT:
            for num_3 in DAY1_INPUT:
                sum_total = num_1 + num_2 + num_3
                if sum_total == num_to_equal:
                    print(f'{num_1} + {num_2} + {num_3} = {sum_total}')
                    print(f'{num_1} * {num_2} + {num_3} = {num_1 * num_2 * num_3}')
                    return
    print(f'No numbers sum together to equal {num_to_equal}')


if __name__ == '__main__':
    sum_two_numbers()
    sum_three_numbers()
