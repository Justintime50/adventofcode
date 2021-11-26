def main():
    with open('adventofcode/input_data/twentytwenty/day5.txt', 'r') as f:
        lines = f.readlines()
    max_id, missing_ids = find_seat_numbers(lines)
    print('Max ID:', max_id)
    print('Missing IDs:', missing_ids)


def find_seat_numbers(boarding_passes):
    """Determines the seat number of a boarding pass.

    Boarding passes look like `FBFBBFFRLR` where the first
    7 characters are the region the seat is in (halfing each time),
    while the last three characters half the row the seat is in.

    Total rows: 128 (0-127)
    Total columns: 8 (0-7)
    """

    seat_ids = []

    for boarding_pass in boarding_passes:
        total_rows = list(range(128))
        row = total_rows
        total_columns = list(range(8))
        column = total_columns
        region_string = boarding_pass[:7]
        row_string = boarding_pass[7:]

        # Check row
        for character in region_string:
            if character.upper() == 'F':
                row = row[: len(row) // 2]
            elif character.upper() == 'B':
                row = row[len(row) // 2 :]

            # Check column
            if len(row) == 1:
                for character in row_string:
                    if character.upper() == 'L':
                        column = column[: len(column) // 2]
                    elif character.upper() == 'R':
                        column = column[len(column) // 2 :]
                # print('Row:', row, 'Column:', column)
                seat_id = (row[0] * 8) + column[0]
                seat_ids.append(seat_id)

    max_id = max(seat_ids)
    sorted_seat_ids = sorted(seat_ids)
    missing_ids = [
        missing_int
        for missing_int in range(sorted_seat_ids[0], sorted_seat_ids[-1] + 1)
        if missing_int not in sorted_seat_ids
    ]

    return max_id, missing_ids


if __name__ == '__main__':
    main()
