from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2023/day1/input.txt')
    answer_1 = get_answer_1(data)
    # answer_2 = get_answer_2(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer_1(data):
    """
    - get the first and last digit of each line, make a two digit number per line, sum all outcomes together
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
        




if __name__ == '__main__':
    main()
