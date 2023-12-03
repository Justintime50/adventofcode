from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2023/day1/input.txt')
    answer_1 = get_answer_1(data)
    answer_2 = get_answer_2(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer_1(data):
    """
    - get the first and last digit of each line, make a two digit number per line, sum all outcomes together
    - This is my initial approach, a better approach is found in answer 2
    """
    sums = []
    for _, line in enumerate(data):
        for char in line:
            if char.isdigit():
                first = char
                break
        for char in line[::-1]:  # Flip the line backwards as a naive way of getting the last digit in the line
            if char.isdigit():
                last = char
                break

        newline = str(first) + str(last)

        sums.append(int(newline))

    return sum(sums)


def get_answer_2(data):
    """
    - get the first and last digit of each line, make a two digit number per line, sum all outcomes together
    - for part 2, there can be words spelled out as well
    - Part 2 help: https://www.youtube.com/watch?v=rnidYOt9m2o
    """
    answer = 0
    for _, line in enumerate(data):
        digits = []
        for char_index, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            for digit, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[char_index:].startswith(value):
                    # Cheating by using the index of the list of spelled out numbers as the stored digits plus one
                    digits.append(str(digit + 1))

        line_score = int(digits[0] + digits[-1])
        answer += line_score

    return answer


if __name__ == '__main__':
    main()
