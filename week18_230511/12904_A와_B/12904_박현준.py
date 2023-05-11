# 31256 KB / 44 ms

S = [x for x in input()]
T = [x for x in input()]

IS_SAME = False


while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] ==  'B':
        T.pop()
        T = T[::-1]
    if S == T:
        IS_SAME = True
        print(1)
        break

if not IS_SAME:
    print(0)