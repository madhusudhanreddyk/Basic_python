months_list = ["jan","feb","mar","apr","may"]
expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter the expense:"))
month = -1
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        month = i
        break
if month != -1:
    print(f'the {expense} is spent in {months_list[i]}')
else:
    print(f'the {expense} was not spent in any month')
