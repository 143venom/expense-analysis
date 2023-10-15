import csv


total_by_expense_type = {}
total_by_payment_method = {}


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


def total_by_Expense_Type():
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense_type = row['expense_type']
            amount_str = row['amount']

            try:
                amount = float(amount_str)
            except ValueError:
                continue

            if expense_type in total_by_expense_type:
                total_by_expense_type[expense_type] += amount
            else:
                total_by_expense_type[expense_type] = amount

    print('Total by Expense Type:')

    for expense_type, total in total_by_expense_type.items():
        print(f'{expense_type}: ${total:.2f}')

def total_by_Payment_Method():
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            payment_method = row['payment_method']
            amount_str = row['amount']

            try:
                amount = float(amount_str)
            except ValueError:
                continue

            if payment_method in total_by_payment_method:
                total_by_payment_method[payment_method] += amount
            else:
                total_by_payment_method[payment_method] = amount

    print('total_by_Payment_Method')

    for payment_method, total in total_by_payment_method.items():
        print(f'{payment_method}: ${total:.2f}')

def main():
    total_Expense()
    total_by_Expense_Type()
    total_by_Payment_Method()

if __name__ == "__main__":
    main()