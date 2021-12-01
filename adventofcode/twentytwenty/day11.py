"""Seat Rules

- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.
- Floor (.) never changes; seats don't move, and nobody sits on the floor.

Recursively run this until no seats change state

QUESTION: How many seats end up occupied?
"""


def main():
    data = open_file()
    generate_seat_map(data)

    # for line in data:
    #     print(line)


class Seat:
    """Parameters represent a direction (top, left, right, bottom)."""

    def __init__(self, line=0, position=0, tl=None, tc=None, tr=None, right=None, br=None, bc=None, bl=None, left=None):
        self.line = line
        self.position = position
        self.tl = tl
        self.tc = tc
        self.tr = tr
        self.right = right
        self.br = br
        self.bc = bc
        self.bl = bl
        self.left = left


def generate_seat_map(data):
    # was_updated = False

    # TODO: The idea is to build unique objects for each seat, run the checks all at once
    # to determine what is changing, change in place, and rinse and repeat till no more seats
    # change. Then you should have your answer. Even with optimizing by creating objects for each
    # seat, I feat this approach is going to be terribly slow with my current implementation.

    for line_num, line in enumerate(data):
        line_positions = list(line)
        for line_position, seat in enumerate(line_positions):
            line_above = data[line_num - 1]
            line_below = data[line_num + 1]

            seat_object = Seat(
                line=line_num,
                position=line_position,
                tl=line_above[line_position - 1],
                tc=line_above[line_position],
                tr=line_above[line_position + 1],
                right=line_positions[line_position + 1],
                br=line_below[line_position + 1],
                bc=line_below[line_position],
                bl=line_below[line_position - 1],
                left=line_positions[line_position - 1],
            )

            print(vars(seat_object))
            break
        break


def open_file():
    with open('adventofcode/input_data/twentytwenty/day11.txt', 'r') as filename:
        data = filename.read()
        split_data = data.split('\n')

        return split_data


if __name__ == '__main__':
    main()
