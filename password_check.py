correct_password="123"
password = input("Enter Password: ")

while correct_password != password:
    password = input("Wrond password! Enter again: ")

print("Logged in")
