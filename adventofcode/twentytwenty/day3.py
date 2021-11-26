import os

RISE = int(os.getenv('RISE', 1))
RUN = int(os.getenv('RUN', 1))


def main():
    part_1 = sled_down_hill(RISE, RUN)
    print(f'Trees hit with a slope of -{RISE}/{RUN}: {part_1}')
    part_2 = part_2_helper()
    print(f'Multiplied trees hit for part 2: {part_2}')


def sled_down_hill(rise, run):
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
        raise ValueError('Rise and Run must be greater than 0')
    with open('adventofcode/input_data/twentytwenty/day3.txt', 'r') as f:
        lines = f.readlines()

    trees_hit = 0
    new_rise = rise
    new_run = run
    for i, line in enumerate(lines):
        if i == new_rise:
            check_index = new_run if i != 0 else 0
            # Prepare the hill line by cascading the length of each line the farther
            # down you go. There is certainly a better way to do this...
            hill_line = (line.strip() + line.strip()) * (i + 1)
            # print(hill_line)
            # print(hill_line[check_index])
            if hill_line[check_index] == '#':
                trees_hit += 1
            new_run = check_index + run
            new_rise += rise
        else:
            continue
    return trees_hit


def part_2_helper():
    """PART TWO

    This simply runs the script multiple times and multiplies the results together
    """
    slope_1 = sled_down_hill(1, 1)
    slope_2 = sled_down_hill(1, 3)
    slope_3 = sled_down_hill(1, 5)
    slope_4 = sled_down_hill(1, 7)
    slope_5 = sled_down_hill(2, 1)
    return slope_1 * slope_2 * slope_3 * slope_4 * slope_5


if __name__ == '__main__':
    main()
