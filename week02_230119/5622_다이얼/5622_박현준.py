S = list(input())
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
res = 0

for i in S:
    for j in dial:
        if i in j:
            res += dial.index(j) + 3
print(res)            