number = int(input("Pick a number!\n"))
numberMod4 = number % 4

if (numberMod4 == 0):
    print("This number is divisible by 4!")
else:
    print(str(number) + " has a remainder of " + str(numberMod4) + " when divided by 4.")
