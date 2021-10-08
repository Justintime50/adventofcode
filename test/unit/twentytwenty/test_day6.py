from adventofcode.twentytwenty.day6 import sum_group_answers


def test_sum_group_answers():
    output_part_1, output_part_2 = sum_group_answers()
    assert output_part_1 == 7027
    assert output_part_2 == 3579
