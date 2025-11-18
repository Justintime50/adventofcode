from adventofcode.utils import open_input


# TODO: This solution can take upwards of 12 seconds to solve which is WAY too slow, there's a better way


def main():
    data = open_input("adventofcode/_2021/day5/input.txt")
    pairs = build_coordinate_pairs(data)

    # We need to find the biggest number in the entire set so we can naively build the diagram x and y size to match
    max_num_in_data = int(max(max([item for item in pairs for item in item], key=lambda x: x[1])))

    diagram = generate_diagram(pairs, max_num_in_data)

    answer_1 = calculate_overlaps(diagram)
    # answer_2 = some_function(data)

    print(answer_1)

    return answer_1


def build_coordinate_pairs(data) -> tuple[list[tuple], list[tuple]]:
    """Builds a list of coordinate pairs and returns them."""
    pairs_data = []
    for line in data:
        # Skip [1] which is the arrow
        pair_one = tuple(line.split()[0].split(","))
        pair_two = tuple(line.split()[2].split(","))

        pairs_data.append([pair_one, pair_two])

    # print(pairs_data)

    return pairs_data


def generate_diagram(pairs: list[tuple], max_num_in_data: int):
    """Generate a diagram of the occurances of line overlaps based on coordinate pairs."""
    # We need to create the diagram and fill it with empty data ('.' = points where no line passed through)
    # before proceeding to fill it with real data
    diagram = []
    for entry in range(max_num_in_data):
        diagram.append(["."] * (max_num_in_data + 2))  # +2 here to deal with index offset
    # print(len(diagram[0]))

    # Iterate over each line of pair data and fill out the diagram
    for line in pairs:
        x1 = int(line[0][0])
        y1 = int(line[0][1])
        x2 = int(line[1][0])
        y2 = int(line[1][1])

        # Skip lines that aren't horizontal or vertical (per part 1)
        if x1 != x2 and y1 != y2:
            continue

        line_direction = "horizontal" if y1 == y2 else "vertical"
        line_to_mark = sorted([x1, x2]) if line_direction == "horizontal" else sorted([y1, y2])
        # print(line_to_mark)

        # Transpose the board for vertical manipulation
        transposed_diagram = list(map(list, zip(*diagram)))
        diagram = transposed_diagram if line_direction == "vertical" else diagram

        for num in range(line_to_mark[0], line_to_mark[1] + 1):
            # first_index is the row
            first_index = y1 if line_direction == "horizontal" else x1
            # second_index is the cell
            second_index = num
            # print(first_index, second_index)
            if diagram[first_index][second_index] == ".":
                diagram[first_index][second_index] = 1
            else:
                diagram[first_index][second_index] += 1

        # Untranspose the diagram for the next iteration?
        transposed_diagram = list(map(list, zip(*diagram)))
        diagram = transposed_diagram if line_direction == "vertical" else diagram

    # for line in diagram:
    #     print(line)

    return diagram


def calculate_overlaps(diagram):
    """Calculate the overlaps on the diagram."""
    flattened_diagram = [item for item in diagram for item in item if isinstance(item, int)]

    # Get all items that have a number more than 1 (AKA: coordinates that have been hit multiple times or "overlap")
    num_overlaps = len([num for num in flattened_diagram if num > 1])

    return num_overlaps


if __name__ == "__main__":
    main()
