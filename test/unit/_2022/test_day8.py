from adventofcode._2022.day8.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 1807
    assert answer2 == 480000
