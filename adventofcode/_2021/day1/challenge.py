def main():
    data = open_input()
    answer_1 = calculate_depth_increase(data, chunk_size=1)
    answer_2 = calculate_depth_increase(data, chunk_size=3)

    print(answer_1, answer_2)

    return answer_1, answer_2


def open_input():
    with open('adventofcode/_2021/day1/input.txt', 'r') as f:
        lines = f.read()

        return lines.split('\n')


def calculate_depth_increase(data: list, chunk_size: str = 3) -> int:
    """Calculate the depth increases from the data in groups of a sliding window of `n` integers.

    - Ensure to cover the bookends of the list due to indicee issues.
    - Lesson learned: make integers integers... weird stuff happened when comparing 10000 to 9992
    and it included some that shouldn't have been included.
    """
    formatted_data = data[:-1]
    depth_increases = 0
    chunk_data = []

    for index, chunk in enumerate(formatted_data):
        chunk_index = 0
        chunk_sum = 0
        while chunk_index < chunk_size:
            try:
                chunk_sum += int(formatted_data[index + chunk_index])
                chunk_index += 1
            except IndexError:
                break

        chunk_data.append(chunk_sum)

    for index, chunk in enumerate(chunk_data):
        if chunk != chunk_data[-1]:
            if chunk < chunk_data[index + 1]:
                # print(chunk, chunk_data[index + 1])  # these should increase every time
                depth_increases += 1

    return depth_increases


if __name__ == '__main__':
    main()
