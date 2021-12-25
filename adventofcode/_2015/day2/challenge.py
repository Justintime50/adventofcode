from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2015/day2/input.txt')
    answer_1, answer_2 = get_answer(data)

    print(answer_1, answer_2)

    return answer_1, answer_2


def get_answer(data):
    total_wrapping_paper_required = total_ribbon_required = 0

    for package in data:
        package_dims = package.lower().split('x')
        length = int(package_dims[0])
        width = int(package_dims[1])
        height = int(package_dims[2])

        length_area = length * width
        width_area = width * height
        height_area = height * length

        # part 1
        total_surface_area = 2 * (length_area + width_area + height_area)
        smallest_size = min(length_area, width_area, height_area)
        total_wrapping_paper_required += total_surface_area + smallest_size

        # part 2
        cubic_area = length * width * height  # the bow is the cubic_area of the package
        sorted_dims = sorted([length, width, height])
        ribbon_required = (sorted_dims[0] * 2) + (sorted_dims[1] * 2)
        total_ribbon_required += ribbon_required + cubic_area

    return total_wrapping_paper_required, total_ribbon_required


if __name__ == '__main__':
    main()
