from adventofcode._2020.day2.challenge import main


def test_input():
    answer_1, answer_2 = main()

    assert answer_1 == 638
    assert answer_2 == 699
