# 2775 부녀회장이 될테야

# 테이블 초기화
graph = [[0] * 15 for _ in range(15)]
for i in range(15):
    graph[0][i] = i

for x in range(1, 15): # x층
    for y in range(1, 15): # y호
        for y1 in range(1, y+1): # x층y호 += (x-1)층[1~y]호
            graph[x][y] += graph[x-1][y1]

# print(*graph[::-1], sep='\n')

T = int(input())

for _ in range(T):
    xx = int(input())
    yy = int(input())
    print(graph[xx][yy])