def sieve_of_eratosthenes(limit):

    # TC : 0( Log Log N)
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            # Update all multiples of num as False (not prime).
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    
    return primes
