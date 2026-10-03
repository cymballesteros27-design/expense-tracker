# Expense Tracker - Installment 3
# Author: Cyrus Ballesteros
# A simple console-based expense tracker that calculates tax and budget .

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your spending, one expense at a time.")
print("=" * 40)

print("MAIN MENU")
print("1. Add an expense\t(coming soon)")
print("2. View all expenses\t(coming soon)") 
print("3. Show total spent\t(coming soon)")
print("4. Exit\t\t(coming soon)")

name = input("What is your name? ")

print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("Enter first expense item: ") 
amount1 = float(input("Enter first expense amount: ")) 
subtotal += amount1

item2 = input("Enter second expense item: ") 
amount2 = float(input("Enter second expense amount: ")) 
subtotal += amount2

average = subtotal / 2 

tax_percent = int(input("Enter tax rate (%): ")) 
tax = subtotal * (tax_percent / 100) 
total = subtotal + tax

budget = float(input("Enter your budget: ")) 
over_budget = total > budget 
left = budget - total

print("-" * 40) 
print("SUMMARY") 
print("-" * 40) 
print(f"Item 1:\t\t{item1}\t₱{amount1:.2f}") 
print(f"Item 2:\t\t{item2}\t₱{amount2:.2f}") 
print(f"Subtotal:\t₱{subtotal:.2f}") 
print(f"Average:\t₱{average:.2f}") 
print(f"Tax ({tax_percent}%):\t₱{tax:.2f}") 
print(f"Grand total:\t₱{total:.2f}") 
print(f"Over budget?\t{over_budget}") 
print(f"Left in budget:\t₱{left:.2f}") 
print("-" * 40)
print("Made by: Cyrus Ballesteros | Installment 3")
print("=" * 40)

