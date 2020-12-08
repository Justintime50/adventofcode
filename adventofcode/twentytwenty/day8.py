def main():
    calculate_num()


def calculate_num():
    """Calculate the answer
    """
    total = 0
    lines_run = []
    total = run_recursion(0, lines_run, total)
    print('Accumulator Value:', total)
    return total


def run_recursion(index, lines_run, total):
    """Recursively iterate through the data to sum the accumulator value
    """
    action, direction, number = format_data()[index]
    index = int(index)

    # print(format_data()[index])
    # print(lines_run)
    if index in lines_run:
        print('Already visited', index, '- stopping!')
        return total

    if action == 'nop':
        lines_run.append(index)
        return run_recursion(index+1, lines_run, total)
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
    """Format the data into a usable structure
    """
    with open('adventofcode/twentytwenty/static_data/day8.txt', 'r') as f:
        lines = f.readlines()

    data = []
    for index, line in enumerate(lines):
        action = line[:3].lower()
        direction = line[4:5].strip()
        number = int(line[5:])
        data.append([action, direction, number])
    # print(data)
    return data


if __name__ == '__main__':
    main()
