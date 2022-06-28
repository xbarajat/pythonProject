import random

GUI_WINDOW_TITLE = "Rock - Paper - Scissors"
WELCOME_MESSAGE  = "Welcome to my First Game created by NINJA!"
GUI_PROMPT_MESSAGE = "Please choose an option:"

WIN_Message = "Congartulations you WON!"
LOSE_Message = "Oh, the Computer won, Its OK!"
TIE_Message = "Its a TIE!"

def random_choice(options=["rock","paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):

    winners = {
        "rock": {
            "rock": None,  # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,  # represents a tie
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,  # represents a tie
        },
    }

    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":

    print("_________________________")
    print("Launching the game.......")
    print("_________________________")

    options = ["rock","paper","scissors"]

    user_choice = input("Please choose either 'rock' 'paper' or 'scissors': ")

    if user_choice in options:
        print("You chose:", user_choice)
    else:
        print(
            "Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.")
        exit()

    computer_choice = random_choice(options)
    print("The computer chose:", computer_choice)
    print("--------------------------")

    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_Message)
        elif winning_choice == computer_choice:
            print(LOSE_Message)
    else:
        print(TIE_Message)

    print("Thanks for playing. Please play again!")

