from adventofcode._2022.day4.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 496
    assert answer2 == 847
