def main():
    data = open_file()
    answer_1 = calculate_position(data)
    answer_2 = calculate_position_with_aim(data)

    print(answer_1, answer_2)


def open_file():
    with open('adventofcode/input_data/twentytwentyone/day2.txt', 'r') as f:
        lines = f.read()

        return lines.split('\n')


def calculate_position(data: list[str]) -> int:
    """Calculate the submarine's position based on the `horizontal_position`
    and it's `depth`, multiplying those numbers together to get the answer.
    """
    horizontal_position = depth = 0

    for instruction in data[:-1]:
        split_data = instruction.split()
        action = split_data[0]
        measurement = int(split_data[1])

        if action == 'forward':
            horizontal_position += measurement
        elif action == 'up':
            depth -= measurement
        elif action == 'down':
            depth += measurement

    answer = horizontal_position * depth

    return answer


def calculate_position_with_aim(data: list[str]) -> int:
    """Calculate the submarine's position based on the `horizontal_position`
    and it's `depth` which is calculated by multiplying the aim and measurement
    then, multiplying those numbers together to get the answer.
    """
    horizontal_position = depth = aim = 0

    for instruction in data[:-1]:
        split_data = instruction.split()
        action = split_data[0]
        measurement = int(split_data[1])

        if action == 'forward':
            horizontal_position += measurement
            depth += aim * measurement
        elif action == 'up':
            aim -= measurement
        elif action == 'down':
            aim += measurement

    answer = horizontal_position * depth

    return answer


if __name__ == '__main__':
    main()
