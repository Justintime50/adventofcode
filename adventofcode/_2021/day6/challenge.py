from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day6/sample.txt')
    school = [int(fish) for fish in data[0].split(',')]

    answer_1 = spawn_new_fish(school, end_sim_day_num=80)

    # TODO: The problem quickly breaks down as `end_sim_day_num` increases.
    # The current algorithm has a Big-O notation of O(n^2) but needs to get to
    # O(n) or better probably, I burned through 55gb of memory usage and 15+ minutes
    # with no answer for PART2 before giving up.
    # answer_2 = spawn_new_fish(school, end_sim_day_num=256)

    print(answer_1)

    return answer_1


def spawn_new_fish(school: list[int], end_sim_day_num: int = 80, day_counter: int = 0) -> int:
    """Spawns a new fish when 1 fish in the "school" reaches a "timer" of 0.

    Returns the number of fish in the school once we reach 'x' days from now.
    """
    new_school = []

    for index, fish in enumerate(school):
        if fish > 0:
            school[index] -= 1
        elif fish == 0:
            school[index] = 6
            new_school.append(8)

    # print(school)
    day_counter += 1
    answer_1 = len(school)  # Assign initially to provide something to return before final return

    while day_counter <= end_sim_day_num:
        school = school + new_school
        answer_1 = len(school)
        return spawn_new_fish(school, end_sim_day_num, day_counter)

    return answer_1


if __name__ == '__main__':
    main()
