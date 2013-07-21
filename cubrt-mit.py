
x = 25     # int(input('Enter an Integer: ')) # prompts for Input


ans = 0 # our guess starts at 0
epsilon = 0.0001
numGuess = 0

##while the cube root of our guess is less than value of x

while ans**3 < abs(x): 
    ans +=1                         #increases the guess by one 
    print('current Guesses=',ans)
    if ans**3 != abs(x):
        while abs(ans**2 - x) >= epsilon and ans <=x:
            ans += 0.0001
            numGuess += 1
            print('NumGuesses=',numGuess)
        if abs(ans**2-x) >= epsilon:
            print('Failed to guess the sq of',x)
        else:
            print(ans,'is close to the Cube root of',x)
            
else:
    if x <0:
        ans = -ans
    print('Cube root of', x,'is',ans)
   
    

