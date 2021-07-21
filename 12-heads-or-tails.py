import random

guess = int(input("I'm going to flip a coin 100 times. How many times do you think it'll land on heads?\n"))
heads = 0
count = 0 

while (count < 100):
    randomNumber = random.randint(0,1)
    if (randomNumber == 0):
        heads = heads + 1
    count = count + 1
if (guess == heads):
    print("Hooray! Your guess of " + str(guess) + " was correct!")
else:
    print("The coin landed on heads " + str(heads) + " times.")
    print("The coin landed on tails " + str(100-heads) + " times.")
