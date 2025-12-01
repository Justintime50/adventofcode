from adventofcode._2025.day1.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 1031
    assert answer2 == 5831
