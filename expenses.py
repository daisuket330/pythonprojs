# expenses = [10.5, 8, 5, 15, 20, 5, 3]
# sum = 0

# for x in expenses:
#     sum = sum + x

total = 0
expenses = []
num_expenses= int(input("enter # of expenses"))
for i in range(num_expenses):
    expenses.append(float(input("enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep='')