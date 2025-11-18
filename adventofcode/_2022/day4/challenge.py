from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day4/input.txt")
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    """
    - pairs of elves split by comma
    - Q: In how many assignment pairs does one range fully contain the other?
    """
    overlapping_part_1 = 0
    overlapping_part_2 = 0
    new_1 = []
    new_2 = []
    for item in data:
        elves = item.split(",")
        pair_1 = elves[0]
        pair_1_min = pair_1.split("-")[0]
        pair_1_max = pair_1.split("-")[1]
        new_1.append((int(pair_1_min), int(pair_1_max)))

        pair_2 = elves[1]
        pair_2_min = pair_2.split("-")[0]
        pair_2_max = pair_2.split("-")[1]
        new_2.append((int(pair_2_min), int(pair_2_max)))

    # print(new)

    # PART 1
    for index, pair in enumerate(new_1):
        min_pair = int(pair[0])
        max_pair = int(pair[1])

        # Both left and right pairs of elves could be contained within each other, check for both
        if (
            min_pair >= int(new_2[index][0])
            and max_pair <= int(new_2[index][1])
            or min_pair <= int(new_2[index][0])
            and max_pair >= int(new_2[index][1])
        ):
            overlapping_part_1 += 1

    # PART 2
    for index, pair in enumerate(new_1):
        min_pair = int(pair[0])
        max_pair = int(pair[1])

        if min_pair <= int(new_2[index][1]) and max_pair >= int(new_2[index][0]):
            overlapping_part_2 += 1

    return overlapping_part_1, overlapping_part_2


if __name__ == "__main__":
    main()
