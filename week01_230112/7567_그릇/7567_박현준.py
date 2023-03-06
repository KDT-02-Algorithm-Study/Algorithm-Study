lst = list(input())
sum = 0
for i in range(len(lst)):
    if i == 0:
        sum += 10
    elif lst[i] == lst[i-1]:
        sum += 5
    else:
        sum += 10
print(sum)