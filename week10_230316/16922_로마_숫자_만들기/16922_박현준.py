# 31256 KB / 44ms

from itertools import combinations_with_replacement
N = int(input())
rome = [1, 5, 10, 50]
dic = {}
for i in combinations_with_replacement(range(4), N):
    sum = 0
    for j in i:
        sum += rome[j]
    dic[sum] = dic.get(0, 1) + 1
print(len(dic))