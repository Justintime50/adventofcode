from adventofcode._2021.day1.challenge import main


def test_challenge():
    answer1, answer2 = main()

    assert answer1 == 1791
    assert answer2 == 1822
