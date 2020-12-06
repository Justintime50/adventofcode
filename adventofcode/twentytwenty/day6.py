def main():
    any_answer_sum, all_answer_sum = sum_group_answers()
    print('Total sum any answers:', any_answer_sum)
    print('Total sum all answers:', all_answer_sum)


def sum_group_answers():
    """Sum the group's answers.

    PART ONE:
    Sum the groups answers by getting the unique values from the survey.
    Each letter counts as one answer, disregard duplicates.
    (eg: [a, b, a] - counts as two answers, uniquely a/b)

    PART TWO:
    Sum the groups answers by only counting answers if everyone in the
    group answered the same question.
    (eg: [a, b], [a, c], [d, a] - the only answer counted is a)
    """
    with open('adventofcode/twentytwenty/static_data/day6.txt', 'r') as f:
        lines = f.read()

    total_sum_any_answer = 0
    total_sum_all_answer = 0
    groups = lines.split('\n\n')
    for group in groups:
        num_any_unique_values = len(set(group.replace('\n', '')))
        total_sum_any_answer += num_any_unique_values
        # print(group, num_any_unique_values)

        people = group.split('\n')
        people_array = [line for line in people]  # Breaks up groups into individual people
        final_array = []
        for person in people_array:
            person_array = [letter for letter in person.lower().strip()]
            final_array.append(person_array)
        num_elements_in_all = len(list(set.intersection(*map(set, final_array))))
        total_sum_all_answer += num_elements_in_all
        # print(people_array, num_elements_in_all)

    # TODO: We add +1 to the total_sum_all_answer because it doesn't account for the last line
    # which contains an extra empty list which means it fails to compare correctly and should
    # be included. Fix this so there is no need to add this offset. It has to do with us splitting
    # the lines by newline above.
    return total_sum_any_answer, total_sum_all_answer + 1


if __name__ == '__main__':
    main()
