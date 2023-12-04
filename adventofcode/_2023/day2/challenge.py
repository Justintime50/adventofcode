from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2023/day2/input.txt')
    answer_1 = get_answer(data)
    # answer_2 = get_answer(data)

    # print(answer_1)
    # print(answer_2)

    return answer_1


def get_answer(data):
    """
    - elf pulls out x num of cubes per round, multiple rounds per game
    - check which games are possible if the "bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes"
    - rounds separated by semi-colons, rounds can contain a variable number of cube combos
    """
    games = []
    for index, line in enumerate(data):
        # Build each game data
        game = []

        unsanatized_rounds = line.split(':')[1].split(';')
        for round_index, cubes in enumerate(unsanatized_rounds):
            cubes_list = cubes.split()
            sanatized_cubes = [entry.replace(',', '') for entry in cubes_list][::-1]
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
        red, green, blue = 0, 0, 0
        for round in game:
            red += round.get('red', 0)
            green += round.get('green', 0)
            blue += round.get('blue', 0)

        # The criteria for a game to be "valid"
        if red <= 12 and green <= 13 and blue <= 14:
            answer += game_index + 1
            print(game_index + 1, game)

    # TODO: This answer of `264` is too low?
    print(answer)


if __name__ == '__main__':
    main()
