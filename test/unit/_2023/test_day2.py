from adventofcode._2023.day2.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 2632
    assert answer2 == 69629
