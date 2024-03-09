import random

choices = ["rock", "paper", "scissors"]


def get_comp_choice():
    """Get computer's choice."""
    comp_choice = random.choice(choices)
    return comp_choice


def get_user_choice():
    """Get user's choice."""
    while True:
        """user_choice = random.choice(choices)"""
        user_choice = input("Make a choice: ").strip().lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def get_winner(user, comp):
    """Determine the winner."""

    if user == comp:
        return "Its a tie!"
    elif (
        (user == "rock" and comp == "scissors")
        or (user == "paper" and comp == "rock")
        or (user == "scissors" and comp == "paper")
    ):
        return "You win"
    else:
        return "You lose"


def main():
    """Main function to run the game."""
    print("Welcome to Rock, Paper, Scissors!")
    print()

    play_again = "yes"

    while play_again.lower() == "yes":
        user = get_user_choice()
        comp = get_comp_choice()
        get_winner(user, comp)

        print(f"You picked {user.capitalize()}.")
        print(f"Computer picked {comp.capitalize()}.")
        play_again = input("Wanna play again. (Yes/No)").strip().lower()


if __name__ == "__main__":
    main()
