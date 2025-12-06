import math

from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day6/input.txt")
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
    operators = [i for i in data[-1].split(" ") if i != ""]
    problems = []
    for index, line in enumerate(data):
        if index + 1 == len(data):
            break

        splitline = line.split()
        problems.extend([] for _ in range(len(splitline)))

        for i, num in enumerate(splitline):
            problems[i].append(num)

    for op_i, op in enumerate(operators):
        if op == "+":
            total += sum([int(i) for i in problems[op_i]])
        elif op == "*":
            total += math.prod([int(i) for i in problems[op_i]])

    return total


if __name__ == "__main__":
    main()
