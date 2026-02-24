import random

while True:

    secret = random.randint(1, 100)   # NEW number per game
    print("New game started!")

    while True:
        guess = int(input("Guess: "))

        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            print("Correct!")
            break

    again = input("Play again? (y/n): ")

    if again.lower() != 'y':
        break