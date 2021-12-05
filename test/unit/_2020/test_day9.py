from adventofcode._2020.day9.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 393911906
    assert answer2 == 59341885
