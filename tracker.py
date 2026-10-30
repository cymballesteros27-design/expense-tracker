# Expense Tracker - Installment 4
# Author: Cyrus Ballesteros
# A simple console-based expense tracker.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print()
print("MAIN MENU")
print("  [1] Add an expense\t\t(coming soon)")
print("  [2] View all expenses\t\t(coming soon)")
print("  [3] Show total spent\t\t(coming soon)")
print("  [4] Exit\t\t\t(coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()
print()

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget

print("-" * 40)
print("SUMMARY")
print(f"  - {item1}: ₱{amount1:.1f}")
print(f"  - {item2}: ₱{amount2:.1f}")
print(f"Subtotal:\t₱{subtotal:.1f}")
print(f"Average:\t₱{average:.1f}")
print(f"Tax ({tax_percent:.1f}%):\t₱{tax:.1f}")
print(f"Grand total:\t₱{total:.1f}")

if over_budget:
    print(f"Over budget by ₱{total - budget:.1f}!")
elif total > budget * 0.90:
    print(f"Careful: only ₱{budget - total:.1f} left.")
else:
    print(f"Within budget. ₱{budget - total:.1f} left.")

print("-" * 40)
print(f"Made by: Cyrus Marc Ballesteros |  Installment 4")
