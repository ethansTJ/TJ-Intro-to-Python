number = int(input("Welcome to Fizz Buzz! Pick a number.\n"))

modThree = number % 3
modFive = number % 5

if (modThree == 0 and modFive == 0):
    print("Fizz buzz!")
elif (modThree == 0):
    print("Fizz!")
elif (modFive == 0):
    print("Buzz!")
else:
    print("Neither fizz nor buzz!")
