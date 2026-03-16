def simulate_prime_discovery(limit):
    """
    An efficient simulation to find all prime numbers up to a limit.
    Shows understanding of algorithmic complexity.
    """
    primes = []
    is_prime = [True] * (limit + 1)
    
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            # Mark multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes

if __name__ == "__main__":
    limit_val = 100
    result = simulate_prime_discovery(limit_val)
    print(f"Scientific Discovery: Found {len(result)} primes below {limit_val}")
    print(f"Primes: {result}")
