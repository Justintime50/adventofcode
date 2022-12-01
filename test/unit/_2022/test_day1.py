from adventofcode._2022.day1.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 70720
    assert answer2 == 207148
