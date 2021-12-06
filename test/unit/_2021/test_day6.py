from adventofcode._2021.day6.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 387413
    assert answer2 == 1738377086345
