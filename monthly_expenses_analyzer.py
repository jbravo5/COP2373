
# This program asks the user to enter their monthly expenses (type and amount),
# then uses reduce to calculate total, highest, and lowest expenses.

from functools import reduce

def get_expenses():
    expenses = []
    again = "yes"
    
    while again.lower() == "yes":
        expense_type = input("Enter expense type: ")
        amount = float(input("Enter expense amount: "))
        
        expenses.append((expense_type, amount))
        
        again = input("Do you want to add another expense? (yes/no): ")
    
    return expenses


def calculate_totals(expenses):
    # Total expense using reduce
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)
    
    # Highest expense using reduce
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)
    
    # Lowest expense using reduce
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)
    
    return total, highest, lowest


def main():
    expenses = get_expenses()
    
    if not expenses:
        print("No expenses entered.")
        return
    
    total, highest, lowest = calculate_totals(expenses)
    
    print("\n----- Expense Summary -----")
    print(f"Total Monthly Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()
