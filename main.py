import random
import os
import sys

def guess_number_game():
    # Set the range for guessing
    number_to_guess = random.randint(1, 10)
    attempts = 3  # Player gets 3 attempts
    
    print("Welcome to the Guessing Game!")
    print("You need to guess a number between 1 and 10.")
    
    # Loop through the number of attempts
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: What's your guess? "))
            
            if guess == number_to_guess:
                print("Congratulations! You've guessed the correct number!")
                return
            
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Too low!")
        
        except ValueError:
            print("Please enter a valid number.")
    
    # If the player runs out of attempts, they lose
    print("Sorry, you lost! The correct number was:", number_to_guess)
    simulate_os_removal()

def simulate_os_removal():
    print("Oh no! You lost the game...")
    print("The OS is being removed... just kidding! 😅")
    
    # Simulate some "OS removal" drama
    for i in range(5, 0, -1):
        print(f"Removing OS in {i} seconds...")
        sys.stdout.flush()
        # time.sleep(1)  # Pause for dramatic effect
    
    print("Your OS is safe! This was just a game after all. Play again?")
    
if __name__ == "__main__":
    guess_number_game()
