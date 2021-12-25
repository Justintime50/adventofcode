from adventofcode._2015.day2.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 1606483
    assert answer2 == 3842356
