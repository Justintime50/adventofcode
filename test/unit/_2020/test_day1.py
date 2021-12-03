from adventofcode._2020.day1.challenge import main


def test_challenge():
    answer1, answer2 = main()

    assert answer1 == 876459
    assert answer2 == 116168640
