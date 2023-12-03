from adventofcode._2023.day1.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 55621
    assert answer2 == 53592
