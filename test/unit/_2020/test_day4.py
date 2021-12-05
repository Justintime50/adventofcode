from adventofcode._2020.day4.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 208
    assert answer2 == 167
