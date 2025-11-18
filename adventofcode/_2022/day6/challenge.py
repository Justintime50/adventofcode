from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day6/input.txt")
    answer_1 = get_answer(data, 4)
    answer_2 = get_answer(data, 14)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data, count: int):
    """
    - start-of-packet marker
    - start of packet: four characters that are all different
    - your subroutine needs to identify the first position where the four most recently
    received characters were all different
    """
    for line in data:
        check = []
        for index, _ in enumerate(line):
            try:
                for num in range(count):
                    check.append(line[index + num])

                index_keeper = []
                for num in range(count):
                    index_keeper.append(index + num)
                    check.append(index_keeper)
            except IndexError:
                pass

            new = set(check[:count])
            if len(new) == count:
                answer = (
                    check[count][count - 1] + 1
                )  # First index is to get the list, second is the get the index of the occurance,
                # then offset by 1 for index errors
                break

            check = []

    return answer


if __name__ == "__main__":
    main()
