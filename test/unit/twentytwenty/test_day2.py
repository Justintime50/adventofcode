from adventofcode.twentytwenty.day2 import iterate_password_data


def test_iterate_password_data():
    valid_password_count_1, valid_password_count_2 = iterate_password_data()
    assert valid_password_count_1 == 638
    assert valid_password_count_2 == 699
