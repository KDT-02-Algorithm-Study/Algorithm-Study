# 25632 소수 부르기 게임
# KB / ms

a, b = map(int, input().split())
c, d = map(int, input().split())

# 최솟값, 최댓값
min_ = min(a, c)
max_ = max(b, d)

g = [1]*(max_+1)
cnt1 = cnt2 = 0

# min~max 에라토스테네스의 체
for i in range(2, int(max_**0.5)+1):
    for j in range(min_, max_+1):
        if j == i:
            continue
        if g[j]:
            if j%i == 0:
                g[j] = 0

# set로 각각의 소수 저장
yt = set([i for i in range(a, b+1) if g[i]])
yj = set([i for i in range(c, d+1) if g[i]])
# 합집합
s = yt.union(yj)
# 각각 원소의 수
yt_l = len(yt)
yj_l = len(yj)
s_l = len(s)

# yj 차집합이 더 클 때
if s_l - yt_l > s_l - yj_l:
    print('yj')
# yt 차집합
elif s_l - yt_l < s_l - yj_l:
    print('yt')
# 같을 때 교집합 원소의 수 홀짝 판별
else:
    if s_l-len(yt-yj)-len(yj-yt) & 1:
        print('yt')
    else:
        print('yj')