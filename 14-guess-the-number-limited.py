import random

randomInt = random.randint(1, 10)
guess = int(input("Pick a number between 1 and 100\n"))
numGuesses = 1

while (guess != randomInt and numGuesses < 10): 
    if (guess < randomInt): 
        guess = int(input("Your guess was too low. Pick again!\n"))
    else: 
        guess = int(input("Your guess was too high. Pick again!\n"))
    numGuesses = numGuesses + 1

if (guess == randomInt):
    print("Good job! You guessed the random number with only " + str(numGuesses) + " guesses!")
else:
    print("You ran out of guesses.")
