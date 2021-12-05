from adventofcode._2020.day6.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 7027
    assert answer2 == 3579
