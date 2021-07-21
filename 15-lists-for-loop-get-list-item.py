groceryList = ["bread", "apples", "chocolate", "pizza"]
randomThings = ["cat", "shoes", "bread", "apples", "fish bowl", "chocolate", "pizza"]

for item in randomThings:
    if (item in groceryList):
        print(item)
    else:
        print("'" + item + "' is not on the grocery list..")
