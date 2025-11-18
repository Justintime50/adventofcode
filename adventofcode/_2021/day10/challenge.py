from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2021/day10/sample.txt")
    answer_1 = some_function(data)
    # answer_2 = some_function(data)

    print(answer_1)

    return answer_1


def some_function(data):
    char_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    illegal_char_points = {  # noqa
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    for line in data:
        # if line[-1] in opening_chars:
        #     print('incomplete line:', line)
        #     continue

        for char_index, char in enumerate(line):
            pair_matched = False
            for i in range(char_index, len(line)):
                # print(line[i])
                if line[i] == char_pairs.get(char):
                    pair_matched = True
                    # print('match found')
                    break
                else:
                    # print('corrupted line:', line)
                    pass

            if pair_matched is False:
                print("corrupted line:", line)
                break


if __name__ == "__main__":
    main()
