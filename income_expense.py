from datetime import datetime
import matplotlib.pyplot as plt

def add_record():
    try:
        income = float(input("Enter monthly income: "))
        expense = float(input("Enter monthly expense: "))
        balance = income - expense
        date = datetime.now().strftime("%Y-%m-%d")

        print(f"Monthly balance: {balance}")

        with open("balance_records.txt", "a") as file:
            file.write(f"{date},Income: {income}, Expense: {expense}, Balance: {balance}\n")
        print(f"Record saved successfully on {date}.\n")
    except ValueError:
        print("Invalid input! Please enter numeric values.\n")

def show_records():
    try:
        with open("balance_records.txt", "r") as file:
            records = file.readlines()
            clean_records = [r for r in records if r.startswith(tuple(str(year) for year in range(2000, 2100)))]
            
            if not clean_records:
                print("No valid dated records found.\n")
            else:
                print("\n--- All Income-Expense Records ---")
                for record in clean_records:
                    print(record.strip())
                print()
                analyze_records(clean_records)
    except FileNotFoundError:
        print("No records found. The file does not exist yet.\n")

def analyze_records(records):
    try:
        incomes = []
        expenses = []
        balances = []

        for line in records:
            parts = line.strip().split(',')
            income = float(parts[1].split(':')[1])
            expense = float(parts[2].split(':')[1])
            balance = float(parts[3].split(':')[1])

            incomes.append(income)
            expenses.append(expense)
            balances.append(balance)

        print("--- STATISTICAL SUMMARY ---")
        print(f"Total income: {sum(incomes)}")
        print(f"Total expense: {sum(expenses)}")
        print(f"Average balance: {sum(balances)/len(balances):.2f}")
        print(f"Max expense: {max(expenses)}")
        print(f"Min balance: {min(balances)}")
        print()
    except:
        print("No valid data to analyze.\n")

def show_chart():
    try:
        with open("balance_records.txt", "r") as file:
            lines = file.readlines()
            clean_lines = [line for line in lines if line.startswith(tuple(str(year) for year in range(2000, 2100)))]

            dates = []
            balances = []

            for line in clean_lines:
                parts = line.strip().split(',')
                date = parts[0]
                balance = float(parts[3].split(':')[1])
                dates.append(date)
                balances.append(balance)

            if not dates:
                print("No data to plot.\n")
                return

            plt.figure(figsize=(10,5))
            plt.plot(dates, balances, marker='o', linestyle='-', color='blue')
            plt.title("Monthly Balance Over Time")
            plt.xlabel("Date")
            plt.ylabel("Balance")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.grid(True)
            plt.show()
    except FileNotFoundError:
        print("No records found to plot.\n")
    except Exception as e:
        print(f"Error while plotting: {e}\n")

def menu():
    print("\n--- INCOME-EXPENSE TRACKER ---")
    print("1. Add new income-expense record")
    print("2. Show all records")
    print("3. Show balance chart")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

