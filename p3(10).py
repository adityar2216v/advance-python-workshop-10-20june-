def find_primes_in_range(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    # Example usage:
    start_range = 10
    end_range = 50
    prime_numbers = find_primes_in_range(start_range, end_range)
    print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")

    start_range = 1
    end_range = 10
    prime_numbers = find_primes_in_range(start_range, end_range)
    print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")