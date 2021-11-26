from adventofcode.twentytwenty.day10 import check_each_adapter, get_data, get_joltage


def test_check_each_adapter():
    data = get_data()
    _, joltage_list = get_joltage(data)
    output_part_1 = check_each_adapter(joltage_list)

    assert output_part_1 == 1690
