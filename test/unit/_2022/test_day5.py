from adventofcode._2022.day5.challenge import main


def test_input():
    answer1, answer2 = main()

    assert answer1 == 'TPGVQPFDH'
    assert answer2 == 'DMRDFRHHH'
