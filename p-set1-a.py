bal = 1000.00      #float(input('Balance on the credit Card:'))
anint = 20      #float(input('Annual Interest Rate: '))
minp =3.0          #float(input('Minimum monthly repayment rate as percentage: '))
tpaid=0

##print('Balance=',bal,'\nInterest Rate=',anint,'%', '\
##\nMinimum Monthley payment rate=',minp,'%\n\n')

for i in range(1,13,1):
    #i = i+1
    print('\n\nMonth',i)
    
    mp = (minp/100)* bal
    
    print('monthly Repayment= $'+'{0:.2f}'.format(mp))
    
    mint = (anint/12/100) * bal
    print('Interest Paid= $'+str(round(mint,2)))
    ppd = mp - mint
    print('Principal Paid= $'+str(round(ppd,2)))
    bal = bal-mp
    print('Remaining Balance= $'+str(round(bal,2)))
    tpaid = mp+tpaid
   
print('\n\nRESULT\nTotal amount paid in 12 months= $'+str(round(tpaid,2)))
print('remaining balance= $'+str(round(bal,2)))

