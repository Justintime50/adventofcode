from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2015/day1/input.txt')
    answer_1, answer_2 = get_answer(data)

    print(answer_1, answer_2)

    return answer_1, answer_2


def get_answer(data) -> int:
    floor = position_entered_basement = 0

    for position, i in enumerate(data[0], start=1):
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1

        if floor < 0 and position_entered_basement == 0:
            position_entered_basement = position

    return floor, position_entered_basement


if __name__ == '__main__':
    main()
