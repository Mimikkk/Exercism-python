def prime(n: int) -> int:
    if n <= 0: raise ValueError('Non positive prime')
    if n == 1: return 2
    primes = [2]
    num = 1
    while n > 1:
        num += 2
        if not any(num % p == 0 for p in primes):
            primes.append(num)
            n -= 1

    return primes[-1]
