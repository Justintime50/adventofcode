from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2020/day9/input.txt')
    answer_1 = find_cypher_weakness_part_1(data)
    answer_2 = find_cypher_weakness_part_2(data, int(answer_1))

    print('Xmas Cypher Weakness part 1:', answer_1)
    print('Xmas Cypher Weakness part 2:', answer_2)

    return answer_1, answer_2


def find_cypher_weakness_part_1(data):
    """
    Finds a weakness in the cypher (a number that doesn't follow the rules).

    RULES
    - Preamble of 25 numbers
    - After the preamble, each number should sum to any two of the 25 previous numbers
    - No two numbers will be the same (no 10 and 10)
    - There may be duplicate sums (10+15 and 10+15)

    Find the number which is not the sum of two of the 25 numbers before it
    """
    # Setup the initial preamble
    preamble = []
    for number in data[:25]:
        preamble.append(number)

    # Sum all pairs in preamble
    for number in data[25:]:
        sum_list = []
        for preamble_number_1 in preamble:
            for preamble_number_2 in preamble:
                # No two numbers can be the same in a pair
                if preamble_number_1 == preamble_number_2:
                    continue
                sum_list.append(int(preamble_number_1) + int(preamble_number_2))
        # Check against a set to improve performance
        if int(number) not in set(sum_list):
            return int(number)

        # Shift the preamble by one number
        preamble.append(number)
        del preamble[0]


def find_cypher_weakness_part_2(data, invalid_number):
    """Finds the cypher weakness by finding a contiguous list of numbers
    that add up to the invalid number from part 1
    """
    for index, _ in enumerate(data):
        contiguous_list = []
        for number in data[index:]:
            contiguous_list.append(int(number))
            if sum(contiguous_list) > invalid_number:
                break
            elif len(contiguous_list) > 1 and sum(contiguous_list) == invalid_number:
                answer = max(contiguous_list) + min(contiguous_list)

    return int(answer)


if __name__ == '__main__':
    main()
