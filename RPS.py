import random #importing random module


while True: #iterate loop
    user_action = input("Enter a choice (rock,paper, scissors): ")#take input
    possible_actions = ["rock", "paper", "scissors"]
    #using random function
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")
#display both outputs what is selected by you and computer

#conditions to check who won the game
    if user_action == computer_action:
        print(f"Both players selected {user_action}. Its a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissor! You win")
        else:
            print("Paper covers rock! You Lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Oaoer covers rock! You win!")
        else:
            print("Scissors cut paper! You lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! You win")
        else:
            print("Rock smashes scissors! You lose.")
#take input for playing again
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break