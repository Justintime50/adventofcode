from adventofcode._2021.day4.challenge import main


def test_input():
    answer2 = main()

    # TODO: answer1 is hiding in there but the functions can't currently return both
    # TODO: Make it so that we can run the logic to get the answer for both days here
    # assert answer1 == 12796
    assert answer2 == 18063
