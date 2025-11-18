from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2021/day3/input.txt")
    gamma_rate = calculate_answer1_rating(data, "gamma")
    epsilon_rate = calculate_answer1_rating(data, "epsilon")
    answer_1 = gamma_rate * epsilon_rate

    oxygen_rate = calculate_answer2_rating(data, "oxygen")
    co2_rate = calculate_answer2_rating(data, "co2")
    answer_2 = oxygen_rate * co2_rate

    print(answer_1, answer_2)

    return answer_1, answer_2


def calculate_answer1_rating(data: list[str], context: str) -> int:
    """Calculate the gamma/epsilon rating by taking the most common bit in each position and converting to decimal."""
    most_common_bit_binary_number = ""

    transposed_lists = list(map(list, zip(*data)))

    for bit_group in transposed_lists:
        ones = bit_group.count("1")
        zeros = bit_group.count("0")

        if ones >= zeros and context == "gamma":
            most_common_bit_binary_number += "1"
        elif ones < zeros and context == "epsilon":
            most_common_bit_binary_number += "1"
        else:
            most_common_bit_binary_number += "0"

    binary_to_decimal = int(most_common_bit_binary_number, 2)

    return binary_to_decimal


def calculate_answer2_rating(data: list[str], context: str) -> int:
    """Calculate the oxygen/co2 rating by taking the most common bit in each position and converting to decimal."""
    transposed_lists = list(map(list, zip(*data)))

    # Go until we get our answer
    index_removal_counter = 0
    data = data[:-1]  # Can't remember why this was necessary but it is
    while len(data) > 1:
        most_common_int_list = []

        # Get the winners of each bit position
        for bit_group in transposed_lists:
            ones = bit_group.count("1")
            zeros = bit_group.count("0")

            # Rule is the same for both contexts here
            if ones >= zeros:
                most_common_int_list.append("1")
            else:
                most_common_int_list.append("0")

        # Iterate over each item and remove those that don't count until we get 1 left
        if context == "oxygen":
            data[:] = [
                entry for entry in data if entry[index_removal_counter] == most_common_int_list[index_removal_counter]
            ]
        elif context == "co2":
            data[:] = [
                entry for entry in data if entry[index_removal_counter] != most_common_int_list[index_removal_counter]
            ]

        index_removal_counter += 1
        transposed_lists = list(map(list, zip(*data)))  # Reassign this because it's a "rolling" set of data

    binary_to_decimal = int(data[0], 2)

    return binary_to_decimal


if __name__ == "__main__":
    main()
