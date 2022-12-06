from adventofcode._2022.day6.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 1042
    assert answer2 == 2980
