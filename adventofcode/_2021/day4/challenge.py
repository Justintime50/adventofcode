# flake8: noqa
def main():
    data = open_input()
    answer_1 = some_function(data)
    answer_2 = some_function(data)

    print(answer_1, answer_2)

    return answer_1, answer_2


def open_input():
    """Open the input_data file for the day."""
    with open('adventofcode/_2021/day0/input.txt', 'r') as f:
        lines = f.read()

    # TODO: Ensure you skip the last element which is often a blank newline.
    return lines.split('\n')
