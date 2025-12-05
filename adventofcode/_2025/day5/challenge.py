from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2025/day5/input.txt")
    answer_1 = get_answer(data)

    print(answer_1)

    return answer_1


def get_answer(data):
    """
    - ingredient ID ranges followed by newline then IDs to check
    - part 1: sum the IDs that are in any range (inclusive)
    - part 2: ignore IDs, sum inclusive ranges at each increment
    """
    ranges = []
    ids = []
    add_ids = False
    total = 0
    for index, line in enumerate(data):
        if line == "":
            add_ids = True
            continue
        if add_ids:
            ids.append(line.strip())
        else:
            pass
            ra = line.split("-")
            ranges.append([ra[0], ra[1]])

    # part 1
    for id in ids:
        for ra in ranges:
            if int(ra[0]) <= int(id) <= int(ra[1]):
                total += 1
                break

    return total


if __name__ == "__main__":
    main()
