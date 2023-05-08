import random

# Define a list of words to choose from
words = ["python", "computer", "programming", "algorithm", "database", "debugging", "software"]

# Select a random word from the list
word = random.choice(words)

# Define the maximum number of incorrect guesses
max_guesses = 6

# Initialize the list of guessed letters and the number of incorrect guesses
guessed_letters = []
num_guesses = 0

# Loop until the player wins or loses
while True:
    # Print the current state of the hangman figure
    print()
    if num_guesses == 0:
        print(" _____")
        print("|    |")
        print("|")
        print("|")
        print("|")
        print("|______")
    elif num_guesses == 1:
        print(" _____")
        print("|    |")
        print("|    O")
        print("|")
        print("|")
        print("|______")
    elif num_guesses == 2:
        print(" _____")
        print("|    |")
        print("|    O")
        print("|    |")
        print("|")
        print("|______")
    elif num_guesses == 3:
        print(" _____")
        print("|    |")
        print("|    O")
        print("|   /|")
        print("|")
        print("|______")
    elif num_guesses == 4:
        print(" _____")
        print("|    |")
        print("|    O")
        print("|   /|\\")
        print("|")
        print("|______")
    elif num_guesses == 5:
        print(" _____")
        print("|    |")
        print("|    O")
        print("|   /|\\")
        print("|   /")
        print("|______")
    elif num_guesses == 6:
        print(" _____")
        print("|    |")
        print("|    O")
        print("|   /|\\")
        print("|   / \\")
        print("|______")
        print(f"The word was '{word}'. You lose!")
        break

    # Print the current state of the word with underscores for unguessed letters
    print()
    for letter in word:
        if letter in guessed_letters:
            print(f"{letter} ", end="")
        else:
            print("_ ", end="")
    print()

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    elif guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("Correct!")
        if all(letter in guessed_letters for letter in word):
            print(f"The word was '{word}'. You win!")
            break
    else:
        print("Incorrect.")
        num_guesses += 1
