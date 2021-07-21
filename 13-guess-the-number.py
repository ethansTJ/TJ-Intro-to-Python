import random

randomInt = random.randint(1, 100)
guess = int(input("Pick a number between 1 and 100\n"))

while (guess != randomInt): 
    if (guess < randomInt): 
        guess = int(input("Your guess was too low. Pick again!\n"))
    else: 
        guess = int(input("Your guess was too high. Pick again!\n"))

print("Good job! You guessed correctly!")
