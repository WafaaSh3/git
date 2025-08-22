list = ["apple", "banana", "cherry", "grape","kiwi"]
print(list)
print("The first fruite in the list: " + list[0])
print("The last fruite in the list: " + list[-1])
list[1] = "mango"
print(list)
list.insert(2,"watermelon")
print(list)
fruit = input("Enter a fruit name to check if it exist: ")
print(list.count(fruit) != 0)
list.sort()
print(list)
