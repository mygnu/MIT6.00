bal = float(input('Balance on the credit Card:'))
anint = float(input('Annual Interest Rate: '))
minp = float(input('Minimum monthly repayment rate as percentage: '))
tpaid=0

print('Balance=',bal,'\nInterest Rate=',anint,'%', '\
\nMinimum Monthley payment rate=',minp,'%\n\n')

for i in range(1,13,1):
    #i = i+1
    print('\n\nMonth',i)
    
    mp = (minp/100)* bal
    
    print('monthly Repayment= $'+'{0:.2f}'.format(mp)) # using a different function to round up
    
    m_int = (anint/12/100) * bal
    print('Interest Paid= $'+str(round(m_int,2)))
    ppd = mp - m_int
    print('Principal Paid= $'+str(round(ppd,2)))
    bal = (bal-mp) + m_int
    print('Remaining Balance= $'+str(round(bal,2)))
    tpaid = mp+tpaid
   
print('\n\nRESULT\nTotal amount paid in 12 months= $'+str(round(tpaid,2)))
print('remaining balance= $'+str(round(bal,2)))

