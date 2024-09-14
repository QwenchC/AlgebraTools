def count_primes_less_than(n):
    """计算小于 n 的素数个数"""
    if n < 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n, start):
                sieve[i] = False
    return sum(sieve)
