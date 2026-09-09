users = {
    "user1":"password1",
    "user2":"password2",
    "user3":"password3"
}
user = input("Enter Your Username:")
password = input("Enter Your Password:")

if users[user] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")
