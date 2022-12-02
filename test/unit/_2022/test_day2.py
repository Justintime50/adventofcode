from adventofcode._2022.day2.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 9759
    assert answer2 == 12429
