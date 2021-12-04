from adventofcode.utils import open_input


# TODO: Have a single function that can take an argument for how many numbers to sum
def main():
    data = open_input('adventofcode/_2020/day1/input.txt')
    answer_1 = sum_two_numbers(data)
    answer_2 = sum_three_numbers(data)

    print(answer_1, answer_2)

    return answer_1, answer_2


def sum_two_numbers(data):
    """PART ONE

    Sum all numbers from the lines list together
    in pairs of num + num until you find two that
    equal 2020.
    """
    num_to_equal = 2020
    for num_1 in data:
        for num_2 in data:
            formatted_num_1 = int(num_1.strip())
            formatted_num_2 = int(num_2.strip())
            sum_total = formatted_num_1 + formatted_num_2
            # print(sum_total)
            if sum_total == num_to_equal:
                print(f'Part 1 Addition: {formatted_num_1} + {formatted_num_2} = {sum_total}')
                print(
                    f'Part 1 Multiplication: {formatted_num_1} * {formatted_num_2} = {formatted_num_1 * formatted_num_2}'  # noqa
                )

                return formatted_num_1 * formatted_num_2
    print(f'No numbers sum together to equal {num_to_equal}')


def sum_three_numbers(data):
    """PART TWO

    Sum all numbers from the lines list together
    in sets of num + num + num until you find two that
    equal 2020.
    """
    num_to_equal = 2020

    # TODO: This is terrible, there's a better way than a triple nested for loop (this runs very slow)
    for num_1 in data:
        for num_2 in data:
            for num_3 in data:
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

                    return formatted_num_1 * formatted_num_2 * formatted_num_3
    print(f'No numbers sum together to equal {num_to_equal}')


if __name__ == '__main__':
    main()
