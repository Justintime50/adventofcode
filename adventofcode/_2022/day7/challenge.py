from collections import defaultdict

from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day7/input.txt")
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    path = []
    totals = defaultdict(int)
    for line in data:
        split_line = line.split()
        if split_line[1] == "ls":
            continue
        elif split_line[1] == "cd":
            if split_line[2] == "..":
                path.pop()
            else:
                totals[split_line[2]] += 0
                path.append(split_line[2])
        elif split_line[0].isnumeric():
            bytes = int(split_line[0])
            for i in range(len(path) + 1):
                last_dir_on_path = "/".join(path[:i])
                totals[last_dir_on_path] += bytes

    dir_size_criteria = 10_0000
    answer_1 = sum([total for total in totals.values() if total <= dir_size_criteria])

    total_space = 70_000_000
    space_needed = 30_000_000
    free_space = total_space - totals["/"]
    update_space = space_needed - free_space

    answer_2 = min([total for total in totals.values() if total >= update_space])

    return answer_1, answer_2


if __name__ == "__main__":
    main()
