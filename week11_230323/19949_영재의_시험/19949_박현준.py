# 121900 KB / 1456 ms

answer = [int(x) for x in input().split()]
yj = []
ans = 0
def back(depth):
    global ans
    
    if depth == 10:
        cnt = 0
        # 영재의 답이 맞는지 비교
        for i in range(10):
            if answer[i] == yj[i]:
                cnt +=1
        # 5개 이상이면 통과
        if cnt >= 5:
            ans += 1
        return
    
    for i in range(1, 6):
        # depth-2가 음수면 안되기에 depth 1부터 시작
        # 같은 답 3개 방지
        if depth > 1 and yj[depth-2] == yj[depth-1] == i:
            continue
        yj.append(i)
        back(depth+1)
        yj.pop()        
back(0)
print(ans)