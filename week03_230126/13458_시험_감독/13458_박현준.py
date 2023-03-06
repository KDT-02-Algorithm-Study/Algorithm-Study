N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())
total = N
for i in lst:
    i -= B
    if i > 0:
        if i % C:
            total += i // C + 1
        else:
            total += i // C
print(total)