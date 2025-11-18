from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day2/input.txt")
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    """
    PART 1
    - A: rock
    - b: paper
    - c: scissors

    - x: rock
    - y: paper
    - z: scissors

    sum of scores for each round

    1 rock
    2 paper
    3 scis
    0 lost
    3 draw
    6 win

    PART 2
    X = lose
    Y = draw
    Z = win
    """
    points_mapping = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    winning_mappings = {
        "Z": "B",
        "X": "C",
        "Y": "A",
    }
    inverse_win = {v: k for k, v in winning_mappings.items()}

    losing_mappings = {
        "Z": "A",
        "X": "B",
        "Y": "C",
    }
    inverse_lose = {v: k for k, v in losing_mappings.items()}

    draw_mappings = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }
    inverse_draw = {v: k for k, v in draw_mappings.items()}

    win_points = 6
    draw_points = 3
    lose_points = 0

    answer_1_total = 0
    answer_2_total = 0
    for battle in data:
        pieces = battle.split(" ")
        opponent_choice = pieces[0].upper()  # ABC
        my_choice = pieces[1].upper()  # XYZ

        # PART 1
        if winning_mappings[my_choice] == opponent_choice:
            answer_1_total += win_points
        elif draw_mappings[my_choice] == opponent_choice:
            answer_1_total += draw_points
        else:
            answer_1_total += lose_points

        answer_1_total += points_mapping[my_choice]

        # PART 2
        draw_char = "Y"
        win_char = "Z"
        if my_choice == draw_char:
            new_choice = inverse_draw[opponent_choice]
            answer_2_total += points_mapping[new_choice]
            answer_2_total += draw_points
        elif my_choice == win_char:
            new_choice = inverse_win[opponent_choice]
            answer_2_total += points_mapping[new_choice]
            answer_2_total += win_points
        else:
            new_choice = inverse_lose[opponent_choice]
            answer_2_total += points_mapping[new_choice]
            answer_2_total += lose_points

    return answer_1_total, answer_2_total


if __name__ == "__main__":
    main()
