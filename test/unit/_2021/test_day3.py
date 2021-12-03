from adventofcode._2021.day3.challenge import main


def test_challenge():
    answer1, answer2 = main()

    assert answer1 == 3429254
    assert answer2 == 5410338
