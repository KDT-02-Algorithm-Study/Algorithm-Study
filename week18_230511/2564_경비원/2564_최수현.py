# 31256 KB / 40 ms

def opposite(store):
    d, i = store
    # 남,북
    if d in {1, 2}:
        return min((i + me[1] + h), ((w-i) + (w-me[1]) + h))
    # 동,서
    else:
        return min((i + me[1] + w), ((w-i) + (w-me[1]) + w))

def near(store):
    d, i = store
    # 북/서 -> index더하기만 하면 됨
    if {d, me[0]} == {1, 3}:
        return i + me[1]
    
    # 북/동 or 남/서는 index를 더하는 것과 가로/세로에서 index빼고 더할 것을 구분
    elif {d, me[0]} == {1, 4}:
        if d == 1:
            return w - i + me[1]
        else:
            return w - me[1] + i
    elif {d, me[0]} == {2, 3}:
        if d == 2:
            return i + h - me[1]
        else:
            return me[1] + h - i
    # 남/동 -> 가로/세로에서 index 빼고 더하기
    elif {d, me[0]} == {2, 4}:
        return w + h - i - me[1]


# 1 북 / 2 남 / 3 서 / 4 동

w, h = map(int, input().split())
n = int(input())
stores = [tuple(map(int, input().split())) for _ in range(n)]
me = tuple(map(int, input().split()))

ans = 0
for dir, index in stores:
    # 같은 면에 있으면 차이 더해주기
    if dir == me[0]:
        ans += abs(index - me[1])
    else:
        # 반대편에 있는 경우
        if (dir in {1, 2} and me[0] in {1, 2}) or (dir in {3, 4} and me[0] in {3, 4}):
            ans += opposite((dir, index))
        # 인접한 면에 있는 경우
        else:
            ans += near((dir, index))

print(ans)