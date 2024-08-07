import random


def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'


def display_results(user_choice, computer_choice, result):
    """Display the results of the game."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'tie':
        print("It's a tie!")
    elif result == 'win':
        print("You win!")
    else:
        print("Computer wins!")


def display_scores(user_score, computer_score, ties):
    """Display the current scores."""
    print(f"\nScore - You: {user_score} | Computer: {computer_score} | Ties: {ties}")


def main():
    """Main function to run the game with score tracking and play again functionality."""
    user_score = 0
    computer_score = 0
    ties = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        # Get user choice
        while True:
            user_choice = input("\nEnter your choice (rock, paper, or scissors): ").strip().lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                break
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

        # Get computer choice
        computer_choice = get_computer_choice()

        # Determine the result
        result = determine_winner(user_choice, computer_choice)

        # Update scores
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        else:
            ties += 1

        # Display results and scores
        display_results(user_choice, computer_choice, result)
        display_scores(user_score, computer_score, ties)

        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


# Run the game
if __name__ == "__main__":
    main()
