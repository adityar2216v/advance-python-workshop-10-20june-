#program one 
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum += i
    return sum

n = int(input("Enter a positive integer: "))    