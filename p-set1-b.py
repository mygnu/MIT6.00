#!/usr/bin/env python3



balance = 10000 #float(input('Balance on the credit Card:'))
anint = 14 #float(input('Annual Interest Rate: '))

print('Balance= $'+str(balance),'\nInterest Rate= '+str(anint)+'%\n\n')

minimum_pay = 1
def payments(pay,bal):
    for i in range(1,13):
        monthly_int = anint/12
        bal = bal * (1+monthly_int/100)- pay
        #print('month', i,'balance =',round(bal,2))
    return bal

while payments(minimum_pay,balance)> 0:
    minimum_pay +=0.01

rest =round((payments(minimum_pay,balance)),2)
print('minimum monthly payment= $'+str(round(minimum_pay,2)),\
'\nRemaining balance is= $'+str(rest))
