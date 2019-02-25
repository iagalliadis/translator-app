correct_password = "123"
name = input("Enter your name: ")
surname = input("Enter your surname: ")
password = input("Enter Password: ")

while correct_password != password:
    password = input("Wrond password! Enter again: ")

message = "Hi %s %s, you are logged in!" % (name, surname)
print(message)
