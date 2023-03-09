def prime(A, B):
    primes = []
    for i in range(A, B+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i > 1:
            primes.append(i)
    return primes

A, B = map(int, input().split())
C, D = map(int, input().split())

yt = prime(A, B)
yj = prime(C, D)