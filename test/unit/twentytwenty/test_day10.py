from adventofcode.twentytwenty.day10 import (
    get_data,
    get_joltage,
    check_each_adapter,
)


def test_check_each_adapter():
    data = get_data()
    _, joltage_list = get_joltage(data)
    output_part_1 = check_each_adapter(joltage_list)
    assert output_part_1 == 1690
