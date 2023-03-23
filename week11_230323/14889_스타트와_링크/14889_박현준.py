# 123896 KB / 1953 ms

def back(s):
    global res
    if len(lst) == N//2:
        total_1 = 0
        total_2 = 0
        for i in range(N):
            for j in range(i+1, N):
                if i in lst and j in lst:
                    total_1 += (S[i][j] + S[j][i])
                elif i not in lst and j not in lst:
                    total_2 += (S[j][i] + S[i][j])
        tmp = abs(total_1 - total_2)
        res = min(res, tmp)
        return
    for i in range(s, N):
        if i not in lst:
            lst.append(i)
            back(i+1)
            lst.pop()


N = int(input())
S = [[int(x) for x in input().split()] for _ in range(N)]
lst = []
res = 9999999999999999
back(0)
print(res)