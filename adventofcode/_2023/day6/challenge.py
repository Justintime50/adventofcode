import math

from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2023/day6/input.txt")
    answer_1 = get_answer(data)
    answer_2 = get_answer(data, part_2=True)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data, part_2: bool = False):
    """
    - paper describes the record distance and how long you get to race it
    - starting speed of 0mm per ms
    - for each 1ms you hold the button, the boat's speed increases by 1mm per ms
    - determine how many times you could beat the record for each race with different combos, multiply all answers
    """
    # TODO: This function is SLOW, takes ~3 seconds for part two, this is due to us needlessly checking every
    # possibility inbetween the two bookends. A vast performance gain could be made by only checking
    # the low and high ends until you find where games are no longer possible and then taking the difference
    # between those numbers to get your answer so we don't have to iterate two hundred trillion times
    game_results = []
    times = ["".join([i for i in data[0].split()[1:]])] if part_2 else data[0].split()[1:]
    records = ["".join([i for i in data[1].split()[1:]])] if part_2 else data[1].split()[1:]

    for i in range(len(times)):
        time = int(times[i])
        record = int(records[i])
        game_possibilities = 0

        for ii in range(time):
            if ii == 0:
                speed = 0
                time_remaining = time
            elif ii + 1 == time:
                time_remaining = 0
            else:
                speed += 1
                time_remaining -= 1

            distance = speed * time_remaining
            if distance > record:
                game_possibilities += 1

        game_results.append(game_possibilities)

    answer = math.prod(game_results)

    return answer


if __name__ == "__main__":
    main()
