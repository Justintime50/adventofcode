from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2024/day1/input.txt")
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    """
    -
    """
    first = []
    second = []
    count = {}
    for index, line in enumerate(data):
        new_line = line.split()
        col_a = new_line[0]
        col_b = new_line[1]
        if col_b not in count:
            count[col_b] = 1
        else:
            count[col_b] += 1
        first.append(col_a)
        second.append(col_b)

    sorted_list_a = sorted(first)
    sorted_list_b = sorted(second)

    comp = zip(sorted_list_a, sorted_list_b)
    part_1_total = 0
    part_2_total = 0

    # Part 1
    for tup in comp:
        new = abs(int(tup[0]) - int(tup[1]))
        part_1_total += new

    # Part 2
    for i in sorted_list_a:
        if count.get(i):
            sim = int(i) * int(count[i])
            part_2_total += sim

    return part_1_total, part_2_total


if __name__ == "__main__":
    main()
