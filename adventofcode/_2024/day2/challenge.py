from adventofcode.utils import open_input

MIN = 1
MAX = 3


def main():
    data = open_input('adventofcode/_2024/day2/input.txt')
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data, True)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data, part_2=False):
    """
    - Reports must go up OR down, not both
    - Difference in each step must be 1-3
    - Count all rows that meet the criteria
    """
    count = 0
    for index, line in enumerate(data):
        split_line = [int(i) for i in line.split()]  # learned: make ints out of i so sorting in python works
        new_line = [
            int(i) for i in line.split()
        ]  # learned: don't reassign new_line to split_line since it gets altered
        sorted_line = sorted(set(split_line))
        reversed_line = sorted(set(split_line), reverse=True)

        valid = False
        if list(sorted_line) == split_line or list(reversed_line) == split_line:
            valid = True

        for index, i in enumerate(split_line):
            try:
                if not MIN <= abs(int(i) - int(split_line[index + 1])) <= MAX:
                    valid = False
                    break
            except IndexError:
                pass

        if part_2 and not valid and (len(new_line) == len(sorted_line) - 1 or len(new_line) == len(reversed_line) - 1):
            valid = True

        if valid:
            # print(line)
            count += 1

    return count


if __name__ == '__main__':
    main()
