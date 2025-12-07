from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day7/input.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    -
    """
    total = 0
    start_index = data[0].index("S")
    line_positions = {0: [start_index]}
    for index, line in enumerate(data[1:]):
        index = index + 1  # Account for offsetting starting line
        line_positions[index] = []
        for char_i, char in enumerate(line):
            if line_positions.get(index - 1) and char_i in line_positions[index - 1] and char == "^":
                line_positions[index].append(char_i - 1)
                line_positions[index].append(char_i + 1)
                total += 1
            elif line_positions.get(index - 1) and char_i in line_positions[index - 1]:
                line_positions[index].append(char_i)

    # for line in data:
    #     print(line)

    # print(line_positions)

    return total


if __name__ == "__main__":
    main()
