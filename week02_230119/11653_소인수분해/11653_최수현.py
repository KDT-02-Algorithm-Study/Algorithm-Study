n = k = int(input())
while n > 1:
    for i in range(2, k+1):
        if n % i == 0:
            print(i)
            n /= i
            break