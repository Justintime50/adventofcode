from adventofcode._2021.day2.challenge import main


def test_challenge():
    answer1, answer2 = main()

    assert answer1 == 1635930
    assert answer2 == 1781819478
