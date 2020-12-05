import re


# TODO: Clean up code and practice DRY, create reusable functions for rules that repeate


def main():
    passports = format_passport_data()
    # print(passports)
    num_valid_passports_part_1, num_valid_passports_part_2 = check_valid_passports(passports)
    print('Number of valid passports part 1:', num_valid_passports_part_1)
    print('Number of valid passports part 2:', num_valid_passports_part_2)


def check_valid_passports(passports):
    """Helper function to check if a passport is valid

    Required fields:
    - byr (Birth Year)
    - iyr (Issue Year)
    - eyr (Expiration Year)
    - hgt (Height)
    - hcl (Hair Color)
    - ecl (Eye Color)
    - pid (Passport ID)

    Optional fields:
    - cid (Country ID)
    """
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]
    optional_fields = ['cid']  # noqa

    valid_passports_part_1 = 0
    valid_passports_part_2 = 0
    for passport in passports:
        num_required_fields_present = 0
        for required_field in required_fields:
            if required_field in passport:
                num_required_fields_present += 1
            if num_required_fields_present == len(required_fields):
                valid_passports_part_1 += 1
                if validate_passport_field_data(passport):
                    valid_passports_part_2 += 1
                    # print(sorted(passport.items()))

    return valid_passports_part_1, valid_passports_part_2


def validate_passport_field_data(passport):
    """Validates passport field data based on criteria

    Criteria:
    - byr (Birth Year) - four digits; at least 1920 and at most 2002.
    - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    - hgt (Height) - a number followed by either cm or in:
    - If cm, the number must be at least 150 and at most 193.
    - If in, the number must be at least 59 and at most 76.
    - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    - pid (Passport ID) - a nine-digit number, including leading zeroes.
    - cid (Country ID) - ignored, missing or not.
    """
    valid_passport = True
    if len(passport['byr']) != 4 or not 1920 <= int(passport['byr']) <= 2002:
        valid_passport = False
    if len(passport['iyr']) != 4 or not 2010 <= int(passport['iyr']) <= 2020:
        valid_passport = False
    if len(passport['eyr']) != 4 or not 2020 <= int(passport['eyr']) <= 2030:
        valid_passport = False

    if not re.match(r'\d+(cm|in)', passport['hgt']):
        # Check if digit followed by "cm" or "in"
        valid_passport = False
    elif re.match(r'\d+cm', passport['hgt']):
        # Check validation against "cm"
        if not 150 <= int(passport['hgt'].replace('cm', '')) <= 193:
            valid_passport = False
    elif re.match(r'\d+in', passport['hgt']):
        # Check validation against "in"
        if not 59 <= int(passport['hgt'].replace('in', '')) <= 76:
            valid_passport = False

    if not re.match(r'#[a-f0-9]{6}', passport['hcl']):
        valid_passport = False
    if not re.match(r'(amb|blu|brn|gry|grn|hzl|oth)', passport['ecl']):
        valid_passport = False
    if not re.match(r'^(\d{9})$', passport['pid']):
        valid_passport = False

    if not passport.get('cid'):
        pass

    return valid_passport


def format_passport_data():
    """Helper function to format passport data
    """
    with open('adventofcode/twentytwenty/static_data/day4.txt', 'r') as f:
        lines = f.read()

    passports = lines.split('\n\n')
    formatted_passports = []
    for passport in passports:
        split_passport = str(passport.strip().lower()).split()
        # print(split_passport)
        dictionary_passport = dict(pair.split(':') for pair in split_passport)
        formatted_passports.append(dictionary_passport)

    return formatted_passports


if __name__ == '__main__':
    main()
