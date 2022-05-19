#in this i will be creating a loan  calculator. 
# get the loan details

money_owed = float(input( "how much money do you owe,in dollars?\n"))#50,000
apr = float(input( "What is the annual percentage rate?\n")) # 3%
payment = float(input( "what will your monthly payent be,in dollars?\n")) # 1,00
months = int(input( "how many months do you wanna see results for?\n")) #24

# divide by 100 to make it a decimal, then divide by 12 to get monthly increments
monthly_rate = apr/100/12

for i in range(months):


    #Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment <0):
        print("The last payment is", money_owed)
        print("You paid off the loan in ", i+1, "months")
        break
    #make payment
    money_owed = money_owed - payment
    #print the results after this 
    print("Paid", payment, "of which", interest_paid, "was interest. ", end='')
    print("Now i owe", money_owed)