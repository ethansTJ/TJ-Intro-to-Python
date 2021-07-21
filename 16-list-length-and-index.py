item = str(input("What would you like to add to your grocery list?\n"))
groceryList = []

while(item.lower() != "done"):
    groceryList.append(item)
    item = str(input("Add another item or enter 'done' if you're done: "))

print("You need to buy " + str(len(groceryList)) + " things. See the list below!\n")
for item in groceryList: 
    print(str(groceryList.index(item) + 1) + ": " + item)
