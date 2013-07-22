prime_l = []
nth_prime = int(input('Enter a number to find n\'th prime: '))
def next_prime(current):
    next_prime = current + 1 # start checking for primes 1 number after the current one
    i = 2
    while next_prime > i: # check with numbers up to next_prime - 1
        if next_prime % i == 0: # if number is divisible
            next_prime += 1 # ready to check the next number
            i = 2 # reset i to check divisibility again from 2
        else:
            i += 1 # increment the divisor
    return next_prime

if __name__ == '__main__':
    current_prime = 2
    while len(prime_l) < nth_prime:
          prime_l.append(current_prime)
          current_prime = next_prime(current_prime)
print('The', str(nth_prime)+'th prime number is', prime_l[-1])
