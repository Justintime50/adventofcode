def main():
    answer_1 = calculate_num()

    return answer_1


def open_input():
    with open('adventofcode/_2020/day8/input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def calculate_num():
    """Calculate the answer"""
    total = 0
    lines_run = []
    total = run_recursion(0, lines_run, total)
    print('Accumulator Value:', total)
    return total


def run_recursion(index, lines_run, total):
    """Recursively iterate through the data to sum the accumulator value"""
    action, direction, number = format_data()[index]
    index = int(index)

    # print(format_data()[index])
    # print(lines_run)
    if index in lines_run:
        print('Already visited', index, '- stopping!')
        return total

    if action == 'nop':
        lines_run.append(index)
        return run_recursion(index + 1, lines_run, total)
    elif action == 'acc':
        if direction == '+':
            total += number
        elif direction == '-':
            total -= number
        lines_run.append(index)
        index += 1
    elif action == 'jmp':
        lines_run.append(index)
        if direction == '+':
            index += number
        elif direction == '-':
            index -= number

    # print('index:', index)
    return run_recursion(index, lines_run, total)


def format_data():
    """Format the data into a usable structure"""
    data = open_input()
    formatted_data = []

    for index, line in enumerate(data):
        action = line[:3].lower()
        direction = line[4:5].strip()
        number = int(line[5:])
        formatted_data.append([action, direction, number])
    # print(formatted_data)
    return formatted_data


if __name__ == '__main__':
    main()
