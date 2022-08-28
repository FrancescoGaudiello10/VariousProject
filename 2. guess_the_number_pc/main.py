import random


def guess_number(x):
    random_number = random.randrange(0, x)
    guess = 0
    count = 0
    while guess != random_number:
        count += 1
        print("[ Tentative n.", count, "]")
        guess = int(input(f"Guess a number between and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly.")
    print("Total numbers of counting ->", count)

guess_number(1000)


# todo: rendere un app a premi questo gioco!
