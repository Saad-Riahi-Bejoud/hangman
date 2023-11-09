import random
# Create a list containing the names of your 5 favorite fruits, and assign this list to a variable called word_list.
word_list = ["watermelon", "strawberry", "melon", "kiwi", "banana"]
# Create the random.choice method and pass the word_list variable into the choice method, and assign it to word variable.
word = random.choice(word_list)
print(word)

# Step 1: Define a function called check_guess and pass the guess as a parameter
def check_guess(guess):
    # Step 2: Convert the guess into lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        
    ask_for_input()
# Step 1: Define a function called ask_for_input
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)


ask_for_input()




