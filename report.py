import csv
from collections import defaultdict


total_by_expense_type = {}
total_by_payment_method = {}
total_by_expense_type = defaultdict(float)
total_by_year_day = defaultdict(float)
total_by_month = [0] * 12
expense_breakdown = {}
payment_method_totals = {'Credit Card': 0, 'Cash': 0, }


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

def top_3_Expense_Types():
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_type = row['expense_type']
            amount_str = row['amount']

            try:
                amount = float(amount_str)
            except ValueError:
                continue

            total_by_expense_type[expense_type] += amount

    sorted_expenses = sorted(
        total_by_expense_type.items(), key=lambda x: x[1], reverse=True)

    print("Top 3 Expense Types:")
    for i, (expense_type, total) in enumerate(sorted_expenses[:3], start=1):
        print(f"{i}. {expense_type}: ${total:.2f}")


def day_with_Highest_Expenses():
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_date = row['expense_date']
            amount_str = row['amount']

            try:
                amount = float(amount_str)
            except ValueError:
                continue

            date_parts = expense_date.split('-')
            if len(date_parts) >= 3:
                year = date_parts[0]
                day = date_parts[-1]
            else:
                continue

            year_day_key = f"{year}-{day}"

            total_by_year_day[year_day_key] += amount

    year_day_with_highest_expenses = max(
        total_by_year_day, key=total_by_year_day.get)
    year_with_highest_expenses, day_with_highest_expenses = year_day_with_highest_expenses.split(
        '-')
    total_expenses_on_highest_day = total_by_year_day[year_day_with_highest_expenses]
    print(
        f"Day with Highest Expenses: {year_with_highest_expenses}, Day {day_with_highest_expenses}, Total Expenses: ${total_expenses_on_highest_day:.2f}")


def month_wise_Total_Expenses():
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_date = row['expense_date']
            amount_str = row['amount']

            try:
                amount = float(amount_str)
            except ValueError:
                continue

            if expense_date.count('-') >= 2:
                _, month, _ = expense_date.split('-')

                month_num = int(month) - 1

                if 0 <= month_num < 12:
                    total_by_month[month_num] += amount

    print("Month-wise Total Expenses:")

    for month_num, total_expenses in enumerate(total_by_month, start=1):
        print(f"{month_num}: ${total_expenses:.2f}")


def expense_Type_Breakdown_by_Payment_Method():
    with open('expenses.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense_type = row['expense_type']
            payment_method = row['payment_method']
            amount_str = row['amount']
            if not expense_type or not payment_method or not amount_str:
                continue

            try:
                amount = float(amount_str)
            except ValueError:
                continue
            if expense_type not in expense_breakdown:
                expense_breakdown[expense_type] = {'Credit Card': 0, 'Cash': 0}

            expense_breakdown[expense_type][payment_method] += amount
            payment_method_totals[payment_method] += amount
    print('Expense Type Breakdown by Payment Method:')
    print(f"{'Expense Type':<15}{'Credit Card':<15}{'Cash':<15}{'Total':<15}")
    print('--------------------------------------------------------------------')
    for expense_type, payment_methods in expense_breakdown.items():
        credit_card_total = payment_methods['Credit Card']
        cash_total = payment_methods['Cash']
        total = credit_card_total + cash_total
        print(
            f"{expense_type:<15}${credit_card_total:.2f}${cash_total:.2f}${total:.2f}")
    print('--------------------------------------------------------------------')
    print(
        f"{'Total':<15}${payment_method_totals['Credit Card']:.2f}${payment_method_totals['Cash']:.2f}")

def main():
    total_Expense()
    total_by_Expense_Type()
    total_by_Payment_Method()
    top_3_Expense_Types()
    day_with_Highest_Expenses()
    month_wise_Total_Expenses()
    expense_Type_Breakdown_by_Payment_Method()

if __name__ == "__main__":
    main()