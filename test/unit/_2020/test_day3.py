from adventofcode._2020.day3.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 148
    assert answer2 == 727923200
