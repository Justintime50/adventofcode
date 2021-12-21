from adventofcode.utils import open_input


def main():
    data = open_input('adventofcode/_2021/day21/input.txt')
    answer_1 = get_answer(data)

    print(answer_1)

    return answer_1


DICE_LIMIT = 100  # the number the dice starts over when it reaches
WINNING_SCORE = 1000
DICE_INCREASE = 1  # the number the dice increases on each roll since it's deterministic
SPACE_TO_RESTART = 10  # restart the count once the player reaches this space


def get_answer(data):
    total_dice_rolls = 0
    dice_roll = 0  # the number the dice is on at the moment, up to `DICE_LIMIT` before restarting at 0

    player1_position = int(data[0].split()[4])
    player1_score = 0
    player2_position = int(data[1].split()[4])
    player2_score = 0

    player1_new_position = player1_position
    player2_new_position = player2_position

    while player1_score < WINNING_SCORE and player2_score < WINNING_SCORE:
        # player1
        dice_roll, total_dice_rolls, player1_new_position, player1_score = roll_dice(
            dice_roll, total_dice_rolls, player1_new_position, player1_score
        )
        if player1_score >= WINNING_SCORE:
            losing_score = player2_score
            break

        # player2
        dice_roll, total_dice_rolls, player2_new_position, player2_score = roll_dice(
            dice_roll, total_dice_rolls, player2_new_position, player2_score
        )
        if player2_score >= WINNING_SCORE:
            losing_score = player1_score
            break

    answer1 = total_dice_rolls * losing_score

    return answer1


def roll_dice(dice_roll: int, total_dice_rolls: int, player_new_position: int, player_score: int):
    num_dice_rolls_per_player = 3
    player_spaces_to_move = 0

    # Setup the dice rolls
    for i in range(num_dice_rolls_per_player):
        dice_roll += DICE_INCREASE
        total_dice_rolls += DICE_INCREASE
        player_spaces_to_move += dice_roll
        if dice_roll == DICE_LIMIT:
            dice_roll = 0

    # Divide the spaces and get the remainder which is the new position once wrapped around
    player_new_position = (player_spaces_to_move + player_new_position) % SPACE_TO_RESTART
    if player_new_position == 0:
        player_new_position = 10

    player_score += player_new_position

    # print(player_spaces_to_move, player_new_position, player_score, total_dice_rolls)

    return dice_roll, total_dice_rolls, player_new_position, player_score


if __name__ == '__main__':
    main()
