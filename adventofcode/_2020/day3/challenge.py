import os

from adventofcode.utils import open_input


RISE = int(os.getenv("RISE", 1))
RUN = int(os.getenv("RUN", 3))


def main():
    data = open_input("adventofcode/_2020/day3/input.txt")
    answer_1 = sled_down_hill(data, RISE, RUN)
    answer_2 = part_2_helper(data)

    print(f"Trees hit with a slope of -{RISE}/{RUN}: {answer_1}")
    print(f"Multiplied trees hit for part 2: {answer_2}")

    return answer_1, answer_2


def sled_down_hill(data, rise, run):
    """PART ONE

    Checks how many trees you'd hit on the way down a slope that looks like
    the following where each tree is a "#":

    ........#.............#........
    ...#....#...#....#.............
    .#..#...#............#.....#..#
    ..#......#..##............###..

    This function sleds down the hill at a specified slope (say -1/3) and
    counts up the number of trees hit on the way down.

    Note: Although RISE is technically negative (going down), the integer
    here must be positive.

    USAGE: RISE=1 RUN=3 venv/bin/python day3.py
    """
    if rise <= 0 or run <= 0:
        raise ValueError("Rise and Run must be greater than 0")

    trees_hit = 0
    new_rise = rise
    new_run = run
    for i, line in enumerate(data):
        if i == new_rise:
            check_index = new_run if i != 0 else 0
            # Prepare the hill line by cascading the length of each line the farther
            # down you go. There is certainly a better way to do this...
            hill_line = (line.strip() + line.strip()) * (i + 1)
            # print(hill_line)
            # print(hill_line[check_index])
            if hill_line[check_index] == "#":
                trees_hit += 1
            new_run = check_index + run
            new_rise += rise
        else:
            continue
    return trees_hit


def part_2_helper(data):
    """PART TWO

    This simply runs the script multiple times and multiplies the results together
    """
    slope_1 = sled_down_hill(data, 1, 1)
    slope_2 = sled_down_hill(data, 1, 3)
    slope_3 = sled_down_hill(data, 1, 5)
    slope_4 = sled_down_hill(data, 1, 7)
    slope_5 = sled_down_hill(data, 2, 1)

    return slope_1 * slope_2 * slope_3 * slope_4 * slope_5


if __name__ == "__main__":
    main()
