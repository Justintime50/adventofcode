from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day9/input.txt")
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    - the tail trails behind the head
    - how many spots did the tail visit at least once (unique cords)?
    """
    tail_visited = set()
    start_cords = (0, 0)
    current_head_cords = start_cords
    last_head_cords = current_head_cords
    current_tail_cords = last_head_cords
    for line in data:
        direction, distance = line.split()

        if direction == "U":
            for i in range(int(distance)):
                # 1. Assign the last cords to them before we change "current" cords
                last_head_cords = current_head_cords

                # 2. Change head cords based on direction
                current_head_cords = (current_head_cords[0], current_head_cords[1] - 1)

                # 3. Make the tail trail by 1 ONLY if there was a gap between head/tail
                if (
                    abs(current_head_cords[0] - current_tail_cords[0]) > 1
                    or abs(current_head_cords[1] - current_tail_cords[1]) > 1
                ):
                    current_tail_cords = last_head_cords
                    tail_visited.add((last_head_cords[0], last_head_cords[1]))

        elif direction == "D":
            for i in range(int(distance)):
                # 1. Assign the last cords to them before we change "current" cords
                last_head_cords = current_head_cords

                # 2. Change head cords based on direction
                current_head_cords = (current_head_cords[0], current_head_cords[1] + 1)

                # 3. Make the tail trail by 1 ONLY if there was a gap between head/tail
                if (
                    abs(current_head_cords[0] - current_tail_cords[0]) > 1
                    or abs(current_head_cords[1] - current_tail_cords[1]) > 1
                ):
                    current_tail_cords = last_head_cords
                    tail_visited.add((last_head_cords[0], last_head_cords[1]))

        elif direction == "L":
            for i in range(int(distance)):
                # 1. Assign the last cords to them before we change "current" cords
                last_head_cords = current_head_cords

                # 2. Change head cords based on direction
                current_head_cords = (current_head_cords[0] - 1, current_head_cords[1])

                # 3. Make the tail trail by 1 ONLY if there was a gap between head/tail
                if (
                    abs(current_head_cords[0] - current_tail_cords[0]) > 1
                    or abs(current_head_cords[1] - current_tail_cords[1]) > 1
                ):
                    current_tail_cords = last_head_cords
                    tail_visited.add((last_head_cords[0], last_head_cords[1]))

        elif direction == "R":
            for i in range(int(distance)):
                # 1. Assign the last cords to them before we change "current" cords
                last_head_cords = current_head_cords

                # 2. Change head cords based on direction
                current_head_cords = (current_head_cords[0] + 1, current_head_cords[1])

                # 3. Make the tail trail by 1 ONLY if there was a gap between head/tail
                if (
                    abs(current_head_cords[0] - current_tail_cords[0]) > 1
                    or abs(current_head_cords[1] - current_tail_cords[1]) > 1
                ):
                    current_tail_cords = last_head_cords
                    tail_visited.add((last_head_cords[0], last_head_cords[1]))

    tail_visited.add(start_cords)
    answer_1 = len(tail_visited)

    return answer_1


if __name__ == "__main__":
    main()
