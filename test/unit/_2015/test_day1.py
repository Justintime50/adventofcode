from adventofcode._2015.day1.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 232
    assert answer2 == 1783
