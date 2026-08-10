# Task 1: Hangman Game
# CodeAlpha Python Programming Internship
# Author: Aryan Pandey

import random

def hangman_game():
    """
    Simple text-based Hangman game where the player guesses a word one letter at a time.
    """
    # List of 5 predefined words
    words = ["python", "programming", "hangman", "computer", "algorithm"]
    
    # Select a random word
    word = random.choice(words).lower()
    
    # Track guessed letters and incorrect guesses
    guessed_letters = []
    incorrect_guesses = []
    max_incorrect = 6
    
    print("=" * 50)
    print("Welcome to Hangman!")
    print("=" * 50)
    print(f"The word has {len(word)} letters.")
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")
    
    # Game loop
    while len(incorrect_guesses) < max_incorrect:
        # Display current state
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word}")
        print(f"Incorrect guesses: {incorrect_guesses}")
        print(f"Remaining guesses: {max_incorrect - len(incorrect_guesses)}")
        
        # Check if player has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You won!")
            print(f"The word was: {word}")
            return
        
        # Get user input
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter!")
            continue
        
        # Check if guess is correct
        if guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            print(f"Sorry, '{guess}' is not in the word.")
    
    # Game over - player lost
    print("\nGame Over!")
    print(f"The word was: {word}")
    print("Better luck next time!")

def main():
    """Main function to run the hangman game."""
    while True:
        hangman_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing Hangman!")
            break
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()