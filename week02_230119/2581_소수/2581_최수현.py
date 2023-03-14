m = int(input())
n = int(input())

not_prime = [1]
for i in range(2, n+1):
    if i in not_prime:
        continue
    else:
        j = i
        k = 2
        while j * k < n + 1:
            not_prime.append(j*k)
            k += 1

not_prime = list(set(not_prime))
prime = []

for num in range(m, n+1):
    if num not in not_prime:
        prime.append(num)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime), prime[0], sep='\n')