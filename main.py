import os

while True:
    print("=" * 40)
    print("   Senior Citizen Helper")
    print("=" * 40)
    print("1. Login")
    print("2. Voice Assistant")
    print("3. Medicine Reminder")
    print("4. SOS")
    print("5. Weather")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("py -3.13 login.py")

    elif choice == "2":
        os.system("py -3.13 voice.py")

    elif choice == "3":
        os.system("py -3.13 reminder.py")

    elif choice == "4":
        os.system("py -3.13 sos.py")

    elif choice == "5":
        os.system("py -3.13 weather.py")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")