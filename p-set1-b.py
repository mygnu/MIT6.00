#!/usr/bin/env python3

initialBalance = 1000 # input('Balance on the Credit Card:')
interestRate = 15 # input('Interest Rate:')


monthlyPayment = 0
monthlyInterest = interestRate/12/100
balance = initialBalance
numMonths = 0


while balance>0:
    monthlyPayment += 1
    numMonths = 0
    
    
    while numMonths<12 and balance > 0:
        numMonths += 1
        interest = monthlyInterest * balance
        balance -= monthlyPayment
        balance += interest
balance = round(balance,2)


print('Monthly Payment=',monthlyPayment)
print('Number of Months needed:', numMonths)
print('Balance:', balance)











## This is my version of 
# balance = 10000 #float(input('Balance on the credit Card:'))
# anint = 14 #float(input('Annual Interest Rate: '))

# print('Balance= $'+str(balance),'\nInterest Rate= '+str(anint)+'%\n\n')

# minimum_pay = 1
# def payments(pay,bal):
#     for i in range(1,13):
#         monthly_int = anint/12
#         bal = bal * (1+monthly_int/100)- pay
#         #print('month', i,'balance =',round(bal,2))
#     return bal

# while payments(minimum_pay,balance)> 0:
#     minimum_pay +=0.01

# rest =round((payments(minimum_pay,balance)),2)
# print('minimum monthly payment= $'+str(round(minimum_pay,2)),\
# '\nRemaining balance is= $'+str(rest))
