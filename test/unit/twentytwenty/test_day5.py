from adventofcode.twentytwenty.day5 import (
    find_seat_numbers,
)


def test_find_seat_numbers():
    with open('adventofcode/twentytwenty/static_data/day5.txt', 'r') as f:
        lines = f.readlines()
    output_part_1, output_part_2 = find_seat_numbers(lines)
    assert output_part_1 == 822
    assert output_part_2 == [705]
