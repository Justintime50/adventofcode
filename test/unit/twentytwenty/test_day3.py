from adventofcode.twentytwenty.day3 import part_2_helper, sled_down_hill


def test_sled_down_hill():
    output = sled_down_hill(1, 3)
    assert output == 148


def test_part_2_helper():
    output = part_2_helper()
    assert output == 727923200
