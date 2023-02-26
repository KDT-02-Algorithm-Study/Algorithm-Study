# 2309 일곱 난쟁이

from itertools import combinations

data = [int(input()) for _ in range(9)]
coms = combinations(data, 7)

for com in coms:
    if sum(com) == 100:
        print(*sorted(com), sep='\n')
        break


# combinations 없이

data = [int(input()) for _ in range(9)]

for i in range(8):
    for j in range(i+1,9):
        sum_ = data[:i]+data[i+1:j]+data[j+1:]
        # print(sum_, sum(sum_))
        if sum(sum_) == 100:
            break
    if sum(sum_) == 100:
        break
print(*sorted(sum_),sep='\n')