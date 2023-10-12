import csv


def total_Expense():
    total_expense = 0
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount_str = row['amount']
            try:
                amount = float(amount_str)
                total_expense += amount
            except ValueError:
                continue
    print(f'Total Expense: ${total_expense:.2f}')

def main():
    total_Expense()

if __name__ == "__main__":
    main()