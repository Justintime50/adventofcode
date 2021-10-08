import os

STARTING_JOLTS = int(os.getenv('STARTING_JOLTS', 0))


def main():
    data = get_data()
    device_rating, joltage_list = get_joltage(data)
    distribution = check_each_adapter(joltage_list)
    print('Distrubution:', distribution)
    part_2(joltage_list, device_rating)


def get_data():
    """Get the data"""
    with open('adventofcode/twentytwenty/static_data/day10.txt', 'r') as f:
        lines = f.readlines()
    return lines


def get_joltage(data):
    """Get the joltage rating of your device (3 more than the highest number)"""
    joltage = []
    for item in data:
        joltage.append(int(item.replace('\n', '')))
    device_rating = max(joltage) + 3
    # print('Joltage:', device_rating)
    return device_rating, sorted(joltage)


def check_each_adapter(joltage_list):
    """Iterate through each adapter and check it against the joltage list"""
    jolts_to_check = STARTING_JOLTS
    one_jolt_difference = 0
    three_jolt_difference = 0
    for jolt in joltage_list:
        difference = jolt - joltage_list[jolts_to_check - 1]
        # print('difference:', difference)
        jolts_to_check += 1
        if difference == 1:
            one_jolt_difference += 1
        elif difference == 3:
            three_jolt_difference += 1
        else:
            continue
    # TODO: Fix this -- Add one for bad 0->1 difference and one for the last item->my device
    distribution = (one_jolt_difference + 1) * (three_jolt_difference + 1)
    return distribution


def part_2(joltage_list, device_rating):
    """Recursively walk through each attempt and backtrack where necessary
    to build a unique set of ways you can connect each adapter
    """
    # PROBLEMS
    # 1) How do you make this performant
    #   * don't reinvent the wheel, find a solution pre-built
    # 2) How do you keep a list of lists that are already valid so you can properly check and backtrack
    #   * https://docs.python.org/3/library/functools.html#functools.lru_cache
    # 3) How do you try all combination? It's not as if you can simply remove the last index alone
    #   * essentially you can check each item added to an array is within 3 of its neighbors
    pass


if __name__ == '__main__':
    main()
