from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day4/input.txt')
    winning_numbers, boards = build_boards(data)
    answer_1 = iterate_boards(winning_numbers, boards, winning_number_index=0, won_boards=[])

    print(answer_1)

    return answer_1


def build_boards(data):
    """Builds a board that looks like this:

    board = [
        [22, 13, 17, 11, 0]
        [8, 2, 23, 4, 24]
        [21, 9, 14, 16, 7]
        [6, 10, 3, 18, 5]
        [1, 12, 20, 15, 19]
    ]
    """
    winning_numbers = data[0].split(',')  # TODO: This shouldn't be in this function

    # print(winning_numbers)

    board_data_to_be_split = []
    for index, line in enumerate(data[1:]):
        # Grab only the board lines and skip the blanks inbetween each board
        if index % 6 != 0:
            line_list = line.split()
            board_data_to_be_split.append(line_list)

    boards = list(
        zip(*[iter(board_data_to_be_split)] * 5)
    )  # Split boards on every valid 5th row to create a full board

    return winning_numbers, boards


def iterate_boards(
    winning_numbers: list[str], boards: list[list[str]], winning_number_index: int, won_boards: list[list[str]]
):
    """Iterate over all the boards."""
    # Once we have each board, go get the winning one via recursion
    new_boards = []
    for board_index, board in enumerate(boards):
        board = mark_board(board, winning_numbers, winning_number_index)
        board_won, board_unmarked_sum = check_board_for_wins(board)
        # print('')  # For debugging, this gives a line break between boards on output

        if board_won is True:  # PART2
            won_boards.append(board)  # PART2
            # print(won_boards)
            data = open_input('adventofcode/_2021/day4/input.txt')  # PART2
            if len(won_boards) == len(build_boards(data)[1]):  # PART2
                last_number_called = int(winning_numbers[winning_number_index])
                for line in board:
                    print(line)
                print('Last number called:', last_number_called)
                print('Board unmarked sum:', board_unmarked_sum)
                print('Answer 1:', last_number_called * board_unmarked_sum)
                return last_number_called * board_unmarked_sum  # TODO: This isn't actually returning
        else:
            new_boards.append(board)

    winning_number_index += 1
    return iterate_boards(winning_numbers, new_boards, winning_number_index, won_boards)


def mark_board(board: list[list[str]], winning_numbers: list, winning_number_index: int):
    """Marks a board if a number matches a winning number."""
    for line_index, line in enumerate(board):
        for num_index, num in enumerate(line):
            if num == winning_numbers[winning_number_index]:
                board[line_index][num_index] = (
                    num + 'X'
                )  # We append an 'X' here to know we've marked it, we'll later remove it to get our answer
        # print(line)

    return board


def check_board_for_wins(board):
    """Do the actual checking here to see if a board won."""
    transposed_board = list(map(list, zip(*board)))

    # Check if any of the rows are finished (all marked 'X')
    for line in board:
        board_won = all('X' in num for num in line)

        if board_won:
            board_unmarked_sum = sum([int(num.replace('X', '')) for num in board for num in num if 'X' not in num])
            return board_won, board_unmarked_sum

    # Check if the transposed board (columns) are finished (all marked 'X')
    for line in transposed_board:
        board_won = all('X' in num for num in line)

        if board_won:
            board_unmarked_sum = sum([
                int(num.replace('X', '')) for num in transposed_board for num in num if 'X' not in num
            ])
            return board_won, board_unmarked_sum

    return board_won, 0


if __name__ == '__main__':
    main()
