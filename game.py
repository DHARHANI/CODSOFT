import random

def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Game Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("Let's begin!\n")
    
    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        # Check if user wants to quit
        if user_choice == 'quit':
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score} | Ties: {rounds_played - user_score - computer_score}")
            print("Thanks for playing!")
            break
        
        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.\n")
            continue
        
        # Computer selection
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win!"
            user_score += 1
        else:
            result = "Computer wins!"
            computer_score += 1
        
        rounds_played += 1
        
        # Display results
        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        print(result)
        print(f"Current Score - You: {user_score} | Computer: {computer_score} | Ties: {rounds_played - user_score - computer_score}\n")

# Start the game
play_game()
