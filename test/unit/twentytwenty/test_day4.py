from adventofcode.twentytwenty.day4 import check_valid_passports, format_passport_data


def test_check_valid_passports():
    passports = format_passport_data()
    output_part_1, output_part_2 = check_valid_passports(passports)

    assert output_part_1 == 208
    assert output_part_2 == 167
