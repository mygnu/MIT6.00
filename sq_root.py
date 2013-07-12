x = int(input('Enter an Integer: '))

print(x,abs(x))
ans = 0 # our guess starts at 0

##while the cube root of our guess is less than value of x
while ans**3 < abs(x): 
    ans +=1                                         #increases the guess by one 
    print('current Guesses=',ans)
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x <0:
        ans = -ans
    print('Cube root of', x,'is',ans)
