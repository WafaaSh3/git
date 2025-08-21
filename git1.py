name = input("Enter your name:")
notes = input ("Enter your notes:")
with open("notes.txt", "w") as file:
    file.write("Name: "+name+"\n")
    file.write("Notes: "+notes+"\n")
with open("notes.txt", "r") as file:
    print(file.read())
     