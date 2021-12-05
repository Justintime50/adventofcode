from adventofcode._2020.day5.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 822
    assert answer2 == 705
