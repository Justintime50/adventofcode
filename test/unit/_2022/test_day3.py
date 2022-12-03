from adventofcode._2022.day3.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 7997
    assert answer2 == 2545
