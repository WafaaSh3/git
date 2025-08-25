prices = {"apple": 40, "banana": 50, "orange": 60, "grape": 70}
fruit = input("Enter the fruit name: ").lower()
if fruit in prices:
    print(f"The price of {fruit} is {prices[fruit]}$ ")
else:
    print("Sorry, this fruit is not available ! ")
