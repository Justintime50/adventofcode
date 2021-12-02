from adventofcode.twentytwentyone.day2 import (
    calculate_position,
    calculate_position_with_aim,
    open_file,
)


def test_calculate_position():
    data = open_file()
    answer = calculate_position(data)

    assert answer == 1635930


def test_calculate_position_with_aim():
    data = open_file()
    answer = calculate_position_with_aim(data)

    assert answer == 1781819478
