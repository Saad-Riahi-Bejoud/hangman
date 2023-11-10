import random

class Hangman:
    # Step 1: Create an __init__ method with word_list and num_lives as parameters
    def __init__(self, word_list, num_lives=5):
        # Step 2: Initialize attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        # Pick a random word from word_list
        self.word = random.choice(self.word_list)
        # Initialize word_guessed with '_' for each letter not yet guessed
        self.word_guessed = ['_' for _ in range(len(self.word))]
        # Calculate the number of unique letters in the word
        self.num_letters = len(set(self.word))
        
    # Step 1: Define a method called check_guess
    def check_guess(self, guess):
        # Step 1: Convert the guessed letter to lower case
        guess = guess.lower()

        # Step 2: Create an if statement that checks if the guess is in the word
        if guess in self.word:
            # Step 3: Print a message saying "Good guess! {guess} is in the word."
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            # Step 1: Create an else statement
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    # Step 2: Define a method called ask_for_input
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            # Step 2: Create an if statement that runs if the guess is NOT a single alphabetical character
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            # Step 3: Create an elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Step 3: Call the check_guess method and pass the guess as an argument
                self.check_guess(guess)
                # Step 3: Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)
                break
            



if __name__ == "__main__":
    hangman_game = Hangman(["watermelon", "strawberry", "melon", "kiwi", "banana"])
    hangman_game.ask_for_input()
    print(f"Word guessed so far: {' '.join(hangman_game.word_guessed)}")
    print(f"Number of unique letters remaining: {hangman_game.num_letters}")