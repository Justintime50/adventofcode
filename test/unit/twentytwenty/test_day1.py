from adventofcode.twentytwenty.day1 import sum_three_numbers, sum_two_numbers


def test_sum_two_numbers():
    sum_1, sum_2 = sum_two_numbers()

    assert sum_1 == 631
    assert sum_2 == 1389


def test_sum_three_numbers():
    sum_1, sum_2, sum_3 = sum_three_numbers()

    assert sum_1 == 708
    assert sum_2 == 140
    assert sum_3 == 1172
