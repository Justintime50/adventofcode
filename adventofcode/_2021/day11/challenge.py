from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day11/sample.txt')
    answer_1 = some_function(data)
    # answer_2 = some_function(data)

    print(answer_1)

    return answer_1


def some_function(data):
    for line in data:
        line_octopus = [int(i) for i in line]
        for octopus in line_octopus:
            octopus += 1
            print(octopus)

    # print()


if __name__ == '__main__':
    main()
