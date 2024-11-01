import random

# List of words to choose from
word_list = ["python", "development", "hangman", "coding", "project", "algorithm"]

def get_random_word(word_list):
    """Selects a random word from the word list."""
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for unguessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_random_word(word_list)  # Select a random word
    guessed_letters = set()            # Set of correctly guessed letters
    incorrect_guesses = set()           # Set of incorrectly guessed letters
    max_attempts = 6                    # Max incorrect guesses allowed

    print("\nWelcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print(display_word(word, guessed_letters))

    while len(incorrect_guesses) < max_attempts:
        guess = input("Enter a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter. Try another one.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect guess! You have {max_attempts - len(incorrect_guesses)} attempts left.")

        print(display_word(word, guessed_letters))
        
        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("Sorry, you've run out of attempts. The word was:", word)

def play_game():
    while True:
        hangman()  # Play one round of Hangman
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thank you for playing Hangman! Goodbye!")
            break

# Run the game
play_game()
