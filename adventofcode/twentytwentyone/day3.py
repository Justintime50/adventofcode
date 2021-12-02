def main():
    data = open_file()
    print(data)


def open_file():
    """Open the input_data file for the day, ensure you skip the last element which is a blank newline."""
    with open('adventofcode/input_data/twentytwentyone/day3.txt', 'r') as f:
        lines = f.read()

        return lines.split('\n')
