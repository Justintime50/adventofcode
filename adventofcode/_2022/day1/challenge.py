from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2022/day1/input.txt')  # TODO: Change this string
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    """
    - Calories
    - Split by newlines per elf
    Prompt Q1: which elf has the most calories
    Prompt Q2: Which 3 elfs have the most combined
    """
    calories_per_elf = []
    elf_calories = 0
    for entry in data:
        if entry == '':
            calories_per_elf.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(entry)

    answer_1 = sorted(calories_per_elf, reverse=True)[0]
    answer_2 = sum(sorted(calories_per_elf, reverse=True)[:3])

    return answer_1, answer_2


if __name__ == '__main__':
    main()
