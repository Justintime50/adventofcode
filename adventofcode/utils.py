def open_input(input_path: str) -> list[str]:
    """Opens and sanitizes the `input.txt` file for the day reading in each line as an element of a list.

    - Remove any extra lines at the end of the input files (if present, due to auto-formatting)
    - Remove newline characters for individual element strings
    """
    with open(input_path, 'r') as f:
        lines = f.readlines()

    line_data = lines[:-1] if lines[-1] == '' else lines
    data = [line_item.replace('\n', '') for line_item in line_data]

    return data


def open_input_literal(input_path: str) -> str:
    """Opens the `input.txt` file literally without sanitizing the data or converting it to a list.

    This should be considered the "legacy" approach or only used when the input data has a structure
    that requires custom parsing.
    """
    with open(input_path, 'r') as f:
        lines = f.read()

    return lines
