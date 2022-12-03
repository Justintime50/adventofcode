import string

from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2022/day3/input.txt')
    answer_1 = get_answer_1(data)
    answer_2 = get_answer_2(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer_1(data):
    """
    - line = rucksack
    - two compartments
    - a vs A is different amount of "points"
    - items (chars) per rucksack
    """
    common = []
    for item in data:
        com_size = int(len(item) / 2)
        com_1 = set(item[:com_size])
        com_2 = set(item[com_size:])

        appear_in_both = com_1 & com_2
        common.append(next(iter(appear_in_both), True))

    points = 0
    offset = 1
    num_chars_in_alph = 26
    for char in common:
        if char.isupper():
            points += string.ascii_uppercase.index(char) + num_chars_in_alph + offset
        else:
            points += string.ascii_lowercase.index(char) + offset

    return points


def get_answer_2(data):
    """
    - sets of 3 rucksacks make a group
    - what's common in a group
    - total num of points
    """
    common = []
    for index, _ in enumerate(data, start=1):
        rucksacks = []
        if index % 3 == 0:
            rucksacks.append(data[index - 1])
            rucksacks.append(data[index - 2])
            rucksacks.append(data[index - 3])

            appear_in_three = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
            common.append(next(iter(appear_in_three), True))

    points = 0
    offset = 1
    num_chars_in_alph = 26
    for char in common:
        if char.isupper():
            points += string.ascii_uppercase.index(char) + num_chars_in_alph + offset
        else:
            points += string.ascii_lowercase.index(char) + offset

    return points


if __name__ == '__main__':
    main()
