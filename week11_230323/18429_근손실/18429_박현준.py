# 31256 KB / 152 ms

def back():
    global cnt
    
    if len(res) == N:
        tmp = 0
        # index를 가지고 중량 증가량을 계산해준다
        for i in res:
            tmp += lst[i]-K
            # 증가량이 음수면 500보다 낮아지므로 return
            if tmp < 0:
                return
        # 아니면 cnt 증가
        else:
            cnt += 1
            return
    # 중량 증가량이 아닌 index의 순열을 res 리스트에 넣는다
    for i in range(N):
        # 중복 방지
        if i not in res:
            res.append(i)
            back()
            res.pop()

N, K = map(int, input().split())
lst = [int(x) for x in input().split()]
res = []
cnt = 0
back()
print(cnt)