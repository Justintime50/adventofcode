from adventofcode._2023.day6.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 6209190
    assert answer2 == 28545089
