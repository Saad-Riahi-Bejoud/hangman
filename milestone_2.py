import random
# Create a list containing the names of your 5 favorite fruits, and assign this list to a variable called word_list.
word_list = ["watermelon", "strawberry", "melon", "kiwi", "banana"]
# Create the random.choice method and pass the word_list variable into the choice method, and assign it to word variable.
word = random.choice(word_list)
# Step 1: Ask the user to enter a single letter
guess = input("Enter a single letter: ")
# Step 2: Check if the input is a single letter and contains only alphabetical characters
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
# Step 3: If the conditions are not met, print an error message
else:
    print("Oops! That is not a valid input.")


