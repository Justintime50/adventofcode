from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2022/day5/input.txt')
    answer_1 = get_answer(data, 1)
    answer_2 = get_answer(data, 2)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data, part):
    """
    - Which ends up on top of each stack
    """
    stack_depth = 0
    stacks = []
    stack = []
    instruction_index_start = 0
    for line_index, line in enumerate(data):
        stack_depth += 1
        if line == '':  # Separate the instructions from stacks
            instruction_index_start = line_index + 1
            break
        for char_index, _ in enumerate(line):
            if line[char_index].isdigit():
                for line_index_up in range(stack_depth):
                    # list order is important, BOTTOM TO TOP = FIRST to LAST
                    try:
                        char_in_question = data[line_index - line_index_up][char_index]
                        if char_in_question == ' ':
                            stack.append('!')  # these are empty spaces
                    except IndexError:
                        pass
                    if char_in_question.isalpha():
                        stack.append(char_in_question)

                    # Once we hit the end, build list
                    if line_index_up + 1 == stack_depth:
                        cleaned_stack = [item for item in stack if item != '!']
                        stacks.append(cleaned_stack)
                        stack = []

    answer = run_instructions(data, instruction_index_start, stacks, part)

    return answer


def run_instructions(data, instruction_index_start, stacks, part):
    instructions = data[instruction_index_start:]
    for line_index, line in enumerate(instructions):
        line_list = line.split(' ')
        quantity = int(line_list[1])
        from_column = int(line_list[3])
        to_column = int(line_list[5])

        try:
            from_items = stacks[from_column - 1]
            to_items = stacks[to_column - 1]
        except IndexError:
            pass

        if part == 1:
            for _ in range(quantity):
                # Take out the last (top) package
                item_to_move = from_items.pop(-1)
                to_items.append(item_to_move)

        if part == 2:
            for times in range(quantity):
                # Do a reverse ordering where when put back in retains the order
                item_to_move = from_items.pop(-quantity + times)
                to_items.append(item_to_move)

    answer = ''
    for stack in stacks:
        answer += stack[-1]

    return answer


if __name__ == '__main__':
    main()
