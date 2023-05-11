# 2564 경비원
# 31256 KB / 44 ms

W, H = map(int, input().split())
n = int(input())

# 위치를 1차원으로 변환 (왼쪽 위 = 0, 시계방향)
def s():
    a, b = map(int, input().split())
    if a == 1:
        return b
    elif a == 2:
        return 2*W+H-b
    elif a == 3:
        return (H+W)*2-b
    else:
        return W+b

store = [] # 상점들의 위치를 저장
for _ in range(n):
    store.append(s())
d = s() # 동근이 위치
r = 0
for i in store:
    # d-i는 반시계 방향 거리
    # d-i가 음수일 때는 시계방향 거리
    # abs(d-i) 가 W+H보다 클 경우는 반대방향이 유리
    if abs(d-i) <= W+H:
        r += abs(d-i)
    else:
        r += (W+H)*2 - abs(d-i)
print(r)