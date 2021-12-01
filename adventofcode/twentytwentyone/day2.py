def main():
    # data = open_file()
    pass


def open_file():
    with open('adventofcode/input_data/twentytwentyone/day2.txt', 'r') as f:
        lines = f.read()

        return lines.split('\n')
