import time
from tkinter import Tk, messagebox

print("=" * 40)
print("      Medicine Reminder")
print("=" * 40)

medicine = input("Enter Medicine Name: ")
reminder_time = input("Enter Reminder Time (HH:MM): ")

print("Reminder Set Successfully!")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == reminder_time:
        root = Tk()
        root.withdraw()

        messagebox.showinfo(
            "Medicine Reminder",
            f"Time to take your medicine!\n\nMedicine: {medicine}"
        )

        break

    time.sleep(30)