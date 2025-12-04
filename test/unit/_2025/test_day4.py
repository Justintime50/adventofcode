from adventofcode._2025.day4.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 1393
    assert answer2 == 8643
