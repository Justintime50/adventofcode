from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day2/input.txt')
    answer_1 = calculate_position(data)
    answer_2 = calculate_position_with_aim(data)

    print(answer_1, answer_2)

    return answer_1, answer_2


def calculate_position(data: list[str]) -> int:
    """Calculate the submarine's position based on the `horizontal_position`
    and it's `depth`, multiplying those numbers together to get the answer.
    """
    horizontal_position = depth = 0

    for instruction in data:
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

    for instruction in data:
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
