import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts.")

count = 0
while True:
    randNum = random.randint(1, 101)
    while count < 7:
        count += 1
        guessNum = int(input("\nEnter your guess : "))
        if guessNum == randNum:
            print(f"Correct! You got it in {count} attempts.")
            print(f"The number was {randNum}")
            break
        elif guessNum > randNum:
            print("Too high!")
        elif guessNum < randNum:
            print("Too low!")
    if guessNum != randNum:
        print("Sorry, you've run out of attempts!")
        print(f"The number was {randNum}")
    retry = input("Play again? (y/n):")
    if retry != "y":
        break




