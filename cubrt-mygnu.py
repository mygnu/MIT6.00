
x = -27 # int(input('Enter an Integer: ')) #  prompts for Input

epsilon = 0.00001
numGuess = 0
low = 0
high = abs(x)
ans = 0 # our guess starts at 0

##while the cube root of our guess is less than value of x

while abs(ans**3 - abs(x)) >= epsilon and ans <= abs(x):
    ans +=1                         #increases the guess by one 
    guess=ans
if ans**3 == abs(x):
    if x <0:
        ans = -ans
    print('Cube root of', x,'is',ans)
    print('number of guesses',guess)

else:    
    ans = (high+low)/2
    while abs(ans**3 - abs(x)) >= epsilon and ans<=abs(x):
        numGuess += 1
        if ans**3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (high+low)/2
    if x <0:
        ans = -ans
    print(ans,'is the closest square root of',x)
    print('number of guesses',numGuess+guess)
