# 3019 테트리스
# 31256 KB / 40 ms

# 블록들의 바닥높이와 회전 data
b1 = [[0], [0, 0, 0, 0]]
b2 = [[0, 0]]
b3 = [[0, 0, 1], [1, 0]]
b4 = [[1, 0, 0], [0, 1]]
b5 = [[0, 0, 0], [0, 1], [1, 0, 1], [1, 0]]
b6 = [[0, 0, 0], [0, 0], [0, 1, 1], [2, 0]]
b7 = [[0, 0, 0], [0, 2], [1, 1, 0], [0, 0]]

bs = [0, b1, b2, b3, b4, b5, b6, b7] # 인덱스로 접근 쉽게

C, P = map(int, input().split())
g = list(map(int, input().split()))

c = 0
for i in bs[P]: # P에 해당하는 인덱스 블록을 탐색
    l = len(i)
    if C < l: # 필드의 너비가 블럭의 너비보다 작으면 countinue
        continue
    for j in range(C-l+1):
        r = g[j:j+l][0] - i[0] # 땅의 높이 - 블록의 바닥높이
        for k in range(1, l):
            if g[j:j+l][k] - i[k] != r: # 처음 값과 달라지면 빈 칸이 발생한것
                break
        else: # break가 발생하지 않으면 count + 1
            c += 1
print(c)