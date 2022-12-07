from adventofcode._2022.day7.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 1513699
    assert answer2 == 7991939
