# TODO: Have a single function that can take an argument for how many numbers to sum


def sum_two_numbers():
    """PART ONE

    Sum all numbers from the lines list together
    in pairs of num + num until you find two that
    equal 2020.
    """
    with open('adventofcode/twentytwenty/static_data/day1.txt', 'r') as f:
        lines = f.readlines()
    num_to_equal = 2020
    for num_1 in lines:
        for num_2 in lines:
            formatted_num_1 = int(num_1.strip())
            formatted_num_2 = int(num_2.strip())
            sum_total = formatted_num_1 + formatted_num_2
            # print(sum_total)
            if sum_total == num_to_equal:
                print(f'Part 1 Addition: {formatted_num_1} + {formatted_num_2} = {sum_total}')
                print(
                    f'Part 1 Multiplication: {formatted_num_1} * {formatted_num_2} = {formatted_num_1 * formatted_num_2}'  # noqa
                )
                return formatted_num_1, formatted_num_2
    print(f'No numbers sum together to equal {num_to_equal}')


def sum_three_numbers():
    """PART TWO

    Sum all numbers from the lines list together
    in sets of num + num + num until you find two that
    equal 2020.
    """
    with open('adventofcode/twentytwenty/static_data/day1.txt', 'r') as f:
        lines = f.readlines()
    num_to_equal = 2020
    for num_1 in lines:
        for num_2 in lines:
            for num_3 in lines:
                formatted_num_1 = int(num_1.strip())
                formatted_num_2 = int(num_2.strip())
                formatted_num_3 = int(num_3.strip())
                sum_total = formatted_num_1 + formatted_num_2 + formatted_num_3
                # print(sum_total)
                if sum_total == num_to_equal:
                    print(f'Part 2 Addition: {formatted_num_1} + {formatted_num_2} + {formatted_num_3} = {sum_total}')
                    print(
                        f'Part 2 Multiplication: {formatted_num_1} * {formatted_num_2} * {formatted_num_3} = {formatted_num_1 * formatted_num_2 * formatted_num_3}'  # noqa
                    )
                    return formatted_num_1, formatted_num_2, formatted_num_3
    print(f'No numbers sum together to equal {num_to_equal}')


if __name__ == '__main__':
    sum_two_numbers()
    sum_three_numbers()
