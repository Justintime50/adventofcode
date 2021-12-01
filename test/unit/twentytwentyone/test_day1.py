from adventofcode.twentytwentyone.day1 import calculate_depth_increase, open_file


def test_calculate_depth_increase_1():
    data = open_file()
    depth_increases = calculate_depth_increase(data, chunk_size=1)

    assert depth_increases == 1791


def test_calculate_depth_increase_3():
    data = open_file()
    depth_increases = calculate_depth_increase(data, chunk_size=3)

    assert depth_increases == 1822
