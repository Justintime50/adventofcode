from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2023/day4/input.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    - you have a list of cards, one set is the winning numbers, one set is your numbers
    - check if you have the winning numbers. You get a point for the first match, then doubled for every match
    """
    answer = 0
    for index, line in enumerate(data):
        sanatized_line = line.split(":")[1].split("|")
        winnings = sanatized_line[0].split()
        my_nums = sanatized_line[1].split()

        points = 0
        for num in my_nums:
            if num in winnings:
                points += 1

        if points == 1:
            answer += 1
        elif points >= 2:
            temp = 1
            for i in range(points - 1):  # -1 hack to account for the 1st iteration not being included here
                temp = temp * 2  # Double the answer for x num of points
            answer += temp

    return answer


if __name__ == "__main__":
    main()
