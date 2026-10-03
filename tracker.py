# Expense Tracker - Installment 2
# Author: Cyrus Ballesteros
# A simple console-based expense tracker that logs 2 expenses.

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
item1 = input("Enter first expense item: ") 
amount1 = float(input("Enter first expense amount: ")) 

item2 = input("Enter second expense item: ") 
amount2 = float(input("Enter second expense amount: ")) 
total = amount1 + amount2 
average = total / 2 

print("-" * 40) 
print("SUMMARY") 
print("-" * 40) 
print(f"Item 1: {item1:<15} ₱{amount1:>10.2f}") 
print(f"Item 2: {item2:<15} ₱{amount2:>10.2f}") 
print(f"Total spent: ₱{total:>10.2f}") 
print(f"Average: ₱{average:>10.2f}") 
print("-" * 40)
print("Made by: Cyrus Ballesteros | Installment 2")
print("=" * 40)

