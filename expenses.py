# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# sum = 0

# for x in expenses:
#     sum = sum + x
    
# print("You spent $", sum, " on lunch this week.", sep='')



# HOW TO USE THE SUM FUNCTION FOR LIST.
# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)

# print("You spent $", total, " on lunch this week.", sep='')



# LOOPS WITH RANGE( ) - ADDING INPUT TO EXPENSES CALCULATOR

# total = 0
# expenses = []
# for i in range (8):
#     expenses.append(float(input("Enter an expense:")))
    
# total = sum(expenses)

# print("You spent $", total, " on lunch this week.", sep='')

# REQUESTING A USER TO INPUT THE NUMBER OF EXPENSES THEY HAVE

total = 0
expenses = []
num_expenses = int(input("Enter the number of expenses:"))
for i in range (num_expenses):
    expenses.append(float(input("Enter an expense:")))
    
total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')