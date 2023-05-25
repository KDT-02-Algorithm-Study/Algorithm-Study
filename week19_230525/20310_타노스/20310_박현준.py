# 31388 KB / 40 ms

S = [x for x in input()]
zero_count = int(S.count('0') / 2)
one_count = int(S.count('1') / 2)
for _ in range(zero_count):
    # S = S[::-1]
    # S.pop(S.index('0'))
    S.pop(-(S[::-1].index('0'))-1)
for _ in range(one_count):
    S.pop(S.index('1'))
print(''.join(S))