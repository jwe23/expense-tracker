import json
import os
from datetime import datetime

EXPENSE_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(EXPENSE_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    """Add a new expense"""
    try:
        amount = float(input("Amount: $"))
        category = input("Category (food/transport/entertainment/bills/other): ").lower()
        description = input("Description: ")
        
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        expenses.append(expense)
        save_expenses(expenses)
        print(f"\n✓ Added ${amount:.2f} to {category}")
        
    except ValueError:
        print("\n✗ Invalid amount. Please enter a number.")

def view_all_expenses(expenses):
    """Display all expenses"""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\n" + "="*60)
    print(f"{'Date':<20} {'Category':<15} {'Amount':<10} Description")
    print("="*60)
    
    for expense in expenses:
        print(f"{expense['date']:<20} {expense['category']:<15} ${expense['amount']:<9.2f} {expense['description']}")
    print("="*60)

def view_total(expenses):
    """Display total spending"""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal spent: ${total:.2f}")

def view_by_category(expenses):
    """Display spending by category"""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    categories = {}
    for expense in expenses:
        category = expense['category']
        categories[category] = categories.get(category, 0) + expense['amount']
    
    print("\n" + "="*40)
    print(f"{'Category':<20} {'Amount'}")
    print("="*40)
    
    for category, amount in sorted(categories.items()):
        print(f"{category:<20} ${amount:.2f}")
    
    print("="*40)
    total = sum(categories.values())
    print(f"{'TOTAL':<20} ${total:.2f}")

def main():
    """Main program loop"""
    expenses = load_expenses()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total")
        print("4. View by category")
        print("5. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_all_expenses(expenses)
        elif choice == '3':
            view_total(expenses)
        elif choice == '4':
            view_by_category(expenses)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\n✗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
