import random

# A list of words that
potential_words = ["Zombie", "Awkward", "Hello", "Beautiful", "Amazing"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_"]*len(word) # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
if len(guess) == 1 and guess not in guesses:
    for i in range(len(word)):
        if word[i] == guess:
            current_word[i] = guess
        loss = False
    guesses.append(guess)

        	# check
#if the guess is correct: Is it in the word? If so, reveal the letters!


    print(current_word)
    fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
