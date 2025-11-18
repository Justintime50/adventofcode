from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2000/day0/sample.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    # print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    -
    """
    for index, line in enumerate(data):
        print(line)


if __name__ == "__main__":
    main()
