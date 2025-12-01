import re

from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day1/input.txt")
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    """
    - Dial starts at 50
    - Dial goes from 0 - 99
    - Password is # of times it points to 0 after each rotation
    - Times seen zero is the number of times we have either passed 0 or landed on it
    """
    dial_position = 50
    password = 0  # part 1
    times_seen_zero = 0  # part 2
    for index, line in enumerate(data):
        combo = re.match(r"([LR])(\d+)", line)
        direction = combo.group(1)
        distance = int(combo.group(2))

        if direction == "L":
            # Go negative
            while distance > 0:
                if dial_position == 0:
                    times_seen_zero += 1
                dial_position -= 1
                distance -= 1
                if dial_position < 0:
                    dial_position = 99
        elif direction == "R":
            # Go positive
            while distance > 0:
                if dial_position == 0:
                    times_seen_zero += 1
                dial_position += 1
                distance -= 1
                if dial_position > 99:
                    dial_position = 0

        if dial_position == 0:
            password += 1

        # print(line, dial_position, password, times_seen_zero)

    return password, times_seen_zero


if __name__ == "__main__":
    main()
