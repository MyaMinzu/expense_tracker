print('===============================')
print('      My expense tracker        ')
print('================================')
expenses = []
try:
    with open('expenses.txt', 'r') as file:
        for line in file:

            data = line.strip().split(',')
            if len(data) == 4:
                data[3] = int(data[3])
                expenses.append(data)

except FileNotFoundError:
    pass

while True:
    print('\n1. Add Expense')
    print('2. View All Expense')
    print('3. View Total Spending')
    print('4. Set Monthly Expense')
    print('5. Exist')

    choice = input('Choose an option (1-5): ')
    if choice == '1':
        print('1. Add Expense')
        date = input('Enter Date (YYYY-MM-DD): ')
        name = input('What did you buy? ')
        category = input('What category did you buy? ')
        price = int(input('Price: '))
        expenses.append([date, name, category, price])
        with open('expenses.txt', 'w') as file:
            for expense in expenses:
                file.write(f'{expense[0]},{expense[1]},{expense[2]},{expense[3]}\n')
        print('Expenses added successfully!')

    elif choice == '2':
        print('2. View All Expense')
        if len(expenses) == 0:
            print('No expenses recorded yet!')
        else:
            print('\n---All Expenses---')
            for expense in expenses:
                print('Date:',expense[0])
                print('Item:',expense[1])
                print('Category:',expense[2])
                print('Price:',expense[3])
                print('--------------------')
    elif choice == '3':
        print('3. View Total Spending')
        total = 0
        for expense in expenses:
            total = total + expense[3]
        print('Total Spending:',total)
    elif choice == '4':
        print('4. Set Monthly Expense')
        budget = int(input('Enter your monthly budget:'))
        total = 0
        for expense in expenses:
            total = total + expense[3]
        remaining = budget - total
        print('Monthly Budget:', budget)
        print('Total Spending:', total)
        print('Remaining Budget:', remaining)
        if remaining == 0:
            print('You are over Budget!!!!!')
        else:
            print('You are within your budget')

    elif choice == '5':
        print('Good Bye!')
        break
    else:
        print('Invalid choice!! Please Try again!')

