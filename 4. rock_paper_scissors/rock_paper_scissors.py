import random


def play():
    user = input("What's your choose? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return "You won!"

    return "you lost!"


def is_win(player, opponent):
    # return true if player wins
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
