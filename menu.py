print("=" * 40)
print("    Senior Citizen Helper Login")
print("=" * 40)

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":

    print("\nLogin Successful!")

    while True:
        print("\n" + "=" * 40)
        print("     Senior Citizen Helper")
        print("=" * 40)
        print("1. Emergency SOS")
        print("2. Medicine Reminder")
        print("3. Voice Assistant")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("🚨 Emergency SOS Activated!")

        elif choice == "2":
            print("💊 Medicine Reminder Started!")

        elif choice == "3":
            print("🎤 Voice Assistant Started!")

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Invalid Username or Password!")