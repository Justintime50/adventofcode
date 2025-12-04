from copy import deepcopy

from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day4/input.txt")
    num_valid = 0
    num_removed = 0
    answer_1, _ = get_answer(data, num_valid, num_removed, part=1)
    _, answer_2 = get_answer(data, num_valid, num_removed, part=2)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data, num_valid, num_removed, part):
    """
    - Find how many rolls of paper (@) can be accessed by a forklift
    - part 1 < 4 adjacent rolls
    - part 2 recursively remove the rolls until you can't anymore, count how many rolls got removed
    """
    copy = deepcopy(data)
    for line_index, line in enumerate(data):
        for char_index, char in enumerate(line):
            if char in [".", "x"]:
                continue
            # Go up
            if line_index == 0:
                ul, uc, ur = False, False, False
            else:
                up_line = data[line_index - 1]
                if char_index == 0:
                    ul = False
                else:
                    ul = up_line[char_index - 1] == "@"
                uc = up_line[char_index] == "@"
                if char_index + 1 == len(line):
                    ur = False
                else:
                    ur = up_line[char_index + 1] == "@"

            # Check current line
            if char_index == 0:
                l = False  # noqa
            else:
                l = line[char_index - 1] == "@"  # noqa
            if char_index + 1 == len(line):
                r = False
            else:
                r = line[char_index + 1] == "@"

            # Go down
            if line_index > 0 and line_index + 1 == len(data):
                dl, dc, dr = False, False, False
            else:
                down_line = data[line_index + 1]
                if char_index == 0:
                    dl = False
                else:
                    dl = down_line[char_index - 1] == "@"
                dc = down_line[char_index] == "@"
                if char_index + 1 == len(line):
                    dr = False
                else:
                    dr = down_line[char_index + 1] == "@"

            is_valid = sum([ul, uc, ur, l, r, dl, dc, dr]) < 4
            if is_valid:
                # part 2
                str_list = list(copy[line_index])
                str_list[char_index] = "x"
                copy[line_index] = str_list
                num_removed += 1

                # part 1
                num_valid += 1
            # print(num_valid)

    # print(num_valid)

    if part == 2:
        # if copy doesn't contain anymore x's, we got to the end
        x_found = False
        for line in copy:
            if "x" in line:
                x_found = True

        if not x_found:
            return num_valid, num_removed

        for line_index, line in enumerate(copy):
            copy[line_index] = "".join(line).replace("x", ".")

        # print(copy)

        return get_answer(copy, num_valid, num_removed, part)
    else:
        return num_valid, num_removed


if __name__ == "__main__":
    main()
