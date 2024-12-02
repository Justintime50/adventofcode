from adventofcode._2024.day1.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 936063
    assert answer2 == 23150395
