from adventofcode.utils import open_input


def main():
    data = open_input("adventofcode/_2022/day8/input.txt")
    answer_1, answer_2 = get_answer(data)

    print(answer_1)
    print(answer_2)

    return answer_1, answer_2


def get_answer(data):
    """
    - 0 small, 9 tall
    - visible form outside the grid for a row or column
    - all on edges are visible
    """
    visible_count = 0
    scenic_scores = []

    # Add edges to visible count
    for index, row in enumerate(data):
        if index == 0 or data[-1] == row:
            visible_count += len(row)
            continue

        if row[0]:
            visible_count += 1
        if row[-1]:
            visible_count += 1

    # Add interior trees (if visible) to visible count
    for row_index, row in enumerate(data):
        if row_index != 0 and row_index != len(data) - 1:
            for tree_index, tree in enumerate(row):
                up_visible = True
                down_visible = True
                left_visible = True
                right_visible = True

                up_count = 0
                down_count = 0
                left_count = 0
                right_count = 0

                if tree_index != 0 and tree_index != len(row) - 1:
                    # Anything from this point on is an interior tree
                    rows_to_top = row_index
                    rows_to_bottom = len(data) - row_index - 1
                    trees_to_left = tree_index
                    trees_to_right = len(row) - tree_index - 1
                    # print(tree, rows_to_top, rows_to_bottom, trees_to_left, trees_to_right)

                    # For every tree, search up all the way to the edge
                    for up in range(rows_to_top):
                        up_count += 1
                        if tree <= data[row_index - up - 1][tree_index]:
                            up_visible = False
                            break

                    # For every tree, search down all the way to the edge
                    for down in range(rows_to_bottom):
                        down_count += 1
                        if tree <= data[row_index + down + 1][tree_index]:
                            down_visible = False
                            break

                    # For every tree, search left all the way to the edge
                    for left in range(trees_to_left):
                        left_count += 1
                        if tree <= row[tree_index - left - 1]:
                            left_visible = False
                            break

                    # For every tree, search right all the way to the edge
                    for right in range(trees_to_right):
                        right_count += 1
                        if tree <= row[tree_index + right + 1]:
                            right_visible = False
                            break

                    # If there is any visibility, the tree can be seen from an edge
                    if any([up_visible, down_visible, left_visible, right_visible]):
                        visible_count += 1

                    scenic_score = up_count * down_count * left_count * right_count
                    scenic_scores.append(scenic_score)

    answer1 = visible_count
    answer2 = max(scenic_scores)

    return answer1, answer2


if __name__ == "__main__":
    main()
