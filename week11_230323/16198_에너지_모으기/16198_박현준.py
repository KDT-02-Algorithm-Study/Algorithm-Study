# 31256 KB / 88 ms

N = int(input())
W = [int(x) for x in input().split()]
res = 0
def back(energy):
    global res

    if len(W) == 2:
        res = max(res, energy)
        return
    
    # N을 1씩 감소, i 앞,뒤로 참조하기에 index 1부터 시작
    for i in range(1, len(W)-1):
        # i 앞, 뒤 더해주기
        tmp = W[i-1] * W[i+1]
        # 해당 i 빼주기
        index = W.pop(i)
        back(tmp + energy)
        # i 다시 넣기
        W.insert(i, index)
back(0)

print(res)