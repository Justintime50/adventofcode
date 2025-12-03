from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day3/input.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    - Need to find the largest number left to right that's 2 digits in a single line
    - TODO: There is a failed attempt at recursion in here for part 2 where a recursion + backoff strategy would
    probably be the play but I ran out of time and care.
    """
    total = 0
    for index, line in enumerate(data):
        line_total = 0
        largest_first = 0
        for i, char in enumerate(line):
            if int(char) > largest_first:
                # If we get to the end, don't accept the final char as largest since we don't have a 2nd
                try:
                    _ = line[i + 1]
                except IndexError:
                    break
                largest_first = int(char)
                index_i = i
            # print(largest_first, index_i)

        line_total = str(largest_first)
        line_total = find_next_num(1, line, index_i, line_total)
        # print(line_total)

        # print(largest_first, largest_second)
        # print(int(f"{largest_first}{largest_second}"))
        total += line_total
    return total


def find_next_num(times, line, index_i, line_total):
    largest_second = 0
    next_index = None
    for offset, char in enumerate(line[index_i + 1 :]):
        if int(char) > largest_second:
            largest_second = int(char)
            next_index = index_i + 1 + offset

    line_total = int(f"{line_total}{largest_second}")
    # print(line_total)

    if len(str(line_total)) >= times or next_index is None:
        # print(line_total, times, next_index)
        return line_total

    return find_next_num(times, line, next_index, line_total)


if __name__ == "__main__":
    main()
