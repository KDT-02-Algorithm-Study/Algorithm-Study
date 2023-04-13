# 2469 사다리 타기
# KB / ms ....ㅠㅜ 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

k = int(input()) # 참가한 사람의 수
n = int(input()) # 가로 막대가 놓일 전체 가로 줄의 수
members = input()
graph = [input() for _ in range(n)]
new_graph = [[]for _ in range(n)]

# 그래프 만들기
for p in range(n):
    for i in range(k-1):
        new_graph[p].append(i)
        new_graph[p].append(graph[p][i])
    new_graph[p].append(k-1)
ppp = 0 
for pp in range(0,len(new_graph[-1]),2):
    new_graph[-1][pp] = ord(members[ppp])-ord('A')
    ppp +=1

# 함수 생성
graph1,graph2 = [],[]
def stage(new_graph2,ng,direc,k):
    next_stage =[0 for _ in range(k)]
    a = 0 
    d0,d1 = 1,-1
    for j in range(0,len(new_graph2),2):
        if j == 0 :
            if new_graph2[j+1] == '-' :
                next_stage[int(j/2) + d0] = new_graph2[2*a]
            else:
                next_stage[0] = new_graph2[2*a]
        elif 0 < j < len(new_graph2)-2:
            if new_graph2[j+1] == '-' :
                next_stage[int(j/2) + d0] = new_graph2[2*a]
            elif new_graph2[j-1] == '-' :
                next_stage[int(j/2) + d1] = new_graph2[2*a]
            else :
                next_stage[int(j/2)] = new_graph2[2*a]
        elif j == len(new_graph2)-1:
            if new_graph2[j-1] == '-' :
                next_stage[int(j/2) + d1] = new_graph2[2*a]
            else :
                next_stage[len(next_stage)-1] = new_graph2[2*a]
        a += 1
    if direc == 0 :
        for n in range(len(next_stage)):
            new_graph[ng+1][2*n] = next_stage[n]
            graph1.append(new_graph[ng+1][2*n])
    elif direc == 1 :
        for n in range(len(next_stage)):
            new_graph[ng-1][2*n] = next_stage[n]
            graph2.append(new_graph[ng-1][2*n])
    return new_graph
# 위에서 아래로
ng = 0 
while True:
    if new_graph[ng][1] == '?':
        break
    else :
        new_graph = stage(new_graph[ng],ng,0,k)
        ng += 1

# 아래에서 위로
ng = n-1
while True:
    if new_graph[ng][1] == '?':
        break
    else :
        new_graph = stage(new_graph[ng],ng,1,k)
        ng -= 1

# 값 비교
compare = [graph1[-k:],graph2[-k:]]
res = [0]

for c in range(k):
    if res[-1] == '-':
        res.append('*')
        continue

    if compare[0][c] == compare[1][c]:
        res.append('*')
    elif compare[0][c] != compare[1][c]:
        if c == 0 :
            if compare[0][c] == compare[1][c+1]:
                res.append('-')
            else : 
                print('x'*(k-1))
                exit(0)
        elif c == k-1 :
            if compare[0][c] == compare[1][c-1]:
                res.append('-')
            else :
                print('x'*(k-1))
                exit(0)
        elif 0 < c < k-1 : 
            if compare[0][c] == compare[1][c-1] or compare[0][c] == compare[1][c+1] :
                res.append('-')
            else :
                print('x'*(k-1))
                exit(0)
print(''.join(res[1:k]))

