print("=" * 40)
print("    Senior Citizen Helper Login")
print("=" * 40)

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("\nLogin Successful!")
else:
    print("\nInvalid Username or Password!")