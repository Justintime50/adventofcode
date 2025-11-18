from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day10/input.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    - `noop` takes 1 cycle
    - `addx` takes 2 cycles
    """
    cycle = 0
    register = 1
    checks = []
    for item in data:
        line = item.split()
        if line[0] == "noop":
            cycle += 1
            check_cycle(cycle, register, checks)
        elif line[0] == "addx":
            for i in range(2):
                cycle += 1
                check_cycle(cycle, register, checks)
                if i == 1:
                    register += int(line[1])

    answer = sum(checks)

    return answer


def check_cycle(cycle, register, checks):
    """Using a function so we can reuse this logic at multiple places in the code."""
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength = register * cycle
        checks.append(signal_strength)


if __name__ == "__main__":
    main()
