from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2023/day2/input.txt")
    answer_1 = get_answer(data)
    answer_2 = get_answer(data, part_2=True)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data, part_2: bool = False):
    """
    part 1:
    - elf pulls out x num of cubes per round, multiple rounds per game
    - check which games are possible if the "bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes"
    - rounds separated by semi-colons, rounds can contain a variable number of cube combos

    part 2:
    - find the least number of cubes needed for each game to be possible, multiply the red/green/blues
    and sum all answers
    """
    games = []
    for index, line in enumerate(data):
        game = []
        unsanatized_rounds = line.split(":")[1].split(";")
        for round_index, cubes in enumerate(unsanatized_rounds):
            cubes_list = cubes.split()
            sanatized_cubes = [entry.replace(",", "") for entry in cubes_list][::-1]
            round_combos = {}
            for entry_index, entry in enumerate(sanatized_cubes):
                # Once we find the color to match with a number, build it
                if not entry.isdigit():
                    # entry here is a color
                    round_combos.update({entry: int(sanatized_cubes[entry_index + 1])})
            game.append(round_combos)
        games.append(game)

    # Check for answer
    answer = 0
    for game_index, game in enumerate(games):
        game_possible = True
        max_red, max_green, max_blue = 0, 0, 0
        for round in game:
            red = round.get("red", 0)
            green = round.get("green", 0)
            blue = round.get("blue", 0)

            # part 2
            if part_2:
                max_red = red if red > max_red else max_red
                max_green = green if green > max_green else max_green
                max_blue = blue if blue > max_blue else max_blue

            # The criteria for a game to be "possible" needs to be checked each round as the cubes go back in the bag
            if not part_2:
                if not red <= 12 or not green <= 13 or not blue <= 14:
                    game_possible = False
                    break

        power = max_red * max_green * max_blue
        answer += power

        if not part_2:
            if game_possible:
                answer += game_index + 1
                # print(game_index + 1, game)

    return answer


if __name__ == "__main__":
    main()
