from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day2/input.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    - can't have leading 0s
    - find all the invalid IDs in a range, add them together for part 1
        - ranges are split by commas
        - IDs cannot repeat themselves (eg: 1010)
    """
    invalid_ids = 0
    for index, line in enumerate(data):
        ranges = line.split(",")
        for range in ranges:
            foo = range.split("-")
            start = int(foo[0])
            end = int(foo[1])
            # print(start, end)
            counter = start
            possibilities = []

            while counter <= end:
                for i, char in enumerate(str(counter)):
                    possibilities.append(str(counter)[: i + 1])
                counter += 1

            unique = set(possibilities)
            # print(unique)
            for i in unique:
                mid = len(str(i)) // 2  # TODO: Part 2 needs to change this
                first_half = i[:mid]
                second_half = i[mid:]
                # print(first_half, second_half)
                if (first_half == second_half) and (start <= int(i) <= end):
                    invalid_ids += int(i)
                    # print(first_half, second_half, "hit")

    return invalid_ids


if __name__ == "__main__":
    main()
