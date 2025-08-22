username =input("Enter your username: ")
password =input("Enter your password: ")

username =username.lower()
print("Your username is:", username)

new_username =username.replace(" ","_")
print("Your Modified username is:", new_username)

print("Your password length is:",len(password) )

print( len(password) >= 8)
print( username == "admin")
print( password == "1234")
print ( username == "admin" and password == "1234")

print (f"Welcome, {new_username}! Your password is {len(password)} characters long.")