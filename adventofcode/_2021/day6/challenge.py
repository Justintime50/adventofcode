from collections import (
    Counter,
    defaultdict,
)

from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day6/input.txt')
    school = [int(fish) for fish in data[0].split(',')]

    answer_1 = spawn_new_fish(school, days_to_spawn_fish=80)
    answer_2 = spawn_new_fish(school, days_to_spawn_fish=256)

    print(answer_1, answer_2)

    return answer_1, answer_2


def spawn_new_fish(school: list[int], days_to_spawn_fish: int = 80) -> int:
    """Spawns a new fish when a fish in the "school" reaches a "timer" of 0.
    Fish will then reset their timer to 7 days from now (6 index), where new
    fish will start their timer at 9 days (8 index).

    Returns the number of fish in the school once we reach 'x' days from now.

    CREDIT: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/6.py
    I really do wish I was smart enough to come up with an answer for this one, but
    my initial solution broke down once `days_to_spawn_fish` passed about `100` because
    I was appending to a list exponentially which was O(n^2). In the end, I learned about
    `Counter` and `defaultdict`, though I wrote the code below by only referencing the
    above for hints on how to use the `collections` module.
    """
    fish_by_timer = Counter(school)

    for day in range(days_to_spawn_fish):
        new_school = defaultdict(int)
        for key, value in fish_by_timer.items():
            if key == 0:
                new_school[6] += value
                new_school[8] += value
            else:
                # If no new fish spawn, knock a day off the timer to new fish spawn for each fish with this timer
                new_school[key - 1] += value

        fish_by_timer = new_school

    number_fish_in_school = sum(fish_by_timer.values())

    return number_fish_in_school


if __name__ == '__main__':
    main()
