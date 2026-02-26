import random
print("Rock Paper Scissors - First to 3 wins!")
while True:
    player_selections = ["Rock", "Paper", "Scissors"]
    choice_map = {
        "r": "Rock",
        "p": "Paper",
        "s": "Scissors"
    }
    #Score
    rounds = 0
    player_score = 0
    computer_score = 0

    while rounds < 5:
        rounds += 1
        print("Round:", rounds)

        player_choice = input("choose (r/p/s): ").lower()

        if player_choice not in choice_map:
            print("Invalid choice!")
            continue

        computer_choice = random.choice(player_selections)
        player_display = choice_map[player_choice]

        print(f"Player : {player_display:10} Computer : {computer_choice}")

        if player_display == computer_choice:
            print("Tie")
        elif (
            (player_display == "Rock" and computer_choice == "Paper") or
            (player_display == "Paper" and computer_choice == "Scissors") or
            (player_display == "Scissors" and computer_choice == "Rock")
        ):
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win this round!")
            player_score += 1
        print(f"\nScore : You : {player_score} Computer : {computer_score}\n")
    if player_score > computer_score:
        print(f"Final Score : You : {player_score} Computer : {computer_score}")
        print("Congratulations! you win the game!")

    elif player_score == computer_score:
        print(f"Final Score : You : {player_score} Computer : {computer_score}")
        print("The game is draw!")

    else:
        print(f"Final Score : You : {player_score} Computer : {computer_score}")
        print("You lose the game!")

    retry = input("Do you want to play again? (y/n): ").lower()
    if retry == "y":
        print("\n")
        continue
    else:
        break



