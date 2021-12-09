from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day9/input.txt')
    answer_1 = find_lowest_points(data)

    # TODO: To get the answer for part2, we can re-use the logic we have for finding the lowest point
    # The lowest point will be in the middle of the basin already. We then need to check outward
    # from the lowest point in every direction (up, down, left, right) until we find all numbers that are
    # sequentially larger than that lowest point
    # answer_2 = find_lowest_points(data)

    print(answer_1)

    return answer_1


def find_lowest_points(data) -> int:
    """Finds the lowest points in a heightmap.

    A `lowest point` refers to a point that is lower (smaller) than numbers directly
    above, below, left, and right of it (diagonals in this situation do not count).

    Returns the `risk_level` (sum of all low points + 1 for every low point) = answer_1
    """
    heightmap = [[int(char) for char in line] for line in data]
    # print(heightmap)
    edge_num = 99  # Make this a large number so we'll include edge numbers as needed
    low_points = []

    for line_index, line in enumerate(heightmap):
        for point_index, point in enumerate(line):
            up = heightmap[line_index - 1][point_index] if line_index > 0 else edge_num
            down = heightmap[line_index + 1][point_index] if line_index + 1 < len(heightmap) else edge_num
            left = heightmap[line_index][point_index - 1] if point_index > 0 else edge_num
            right = heightmap[line_index][point_index + 1] if point_index + 1 < len(line) else edge_num
            # print(up, down, left, right, point)

            if point < up and point < down and point < left and point < right:
                # print('low point:', point)
                low_points.append(point)

    risk_level = sum(low_points) + len(low_points) * 1

    return risk_level


if __name__ == '__main__':
    main()
