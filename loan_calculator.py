
# GET THE LOAN DETAILS
money_owed = float (input("How much money do you owe, in dollars?\n")) #50,000
apr = float(input("What is the annual percentage rate?\n")) #3% #apr-Intrest rate
payment = float(input("What will be your monthly payment be, in dollars?\n")) #$1000
months = int(input("How many months do you want to see results for?\n")) #24

#Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    #Add in intrest
    intrest_paid = money_owed * monthly_rate  #first months intrest then add to the money we owe.
    money_owed = money_owed + intrest_paid  #first months intrest then add to the money we owe.

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break
    
#Make Payment
    money_owed = money_owed - payment
    
#Print the results after this month
    print("Paid", payment, " of which", intrest_paid, " was intrest", end= ' ')
    print("Now i owe", money_owed)



