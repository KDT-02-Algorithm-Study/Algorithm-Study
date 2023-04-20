# 16918 봄버맨
# 33948 KB / 1596 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

r,c,n = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
bomb = []

def find_bomb(graph):
    bomb = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb.append((i,j))
    return bomb,graph

def full_bomb():
    graph = [['O']*c for _ in range(r)]
    return graph


def b_bomb(bomb):
    for i,j in bomb:
        #print(i,j)
        graph[i][j] = '.'        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < r and 0 <= ny < c :
                graph[nx][ny] = '.'
    return graph


# main
init_flag = False

for t in range(1,n+1):
    if init_flag == False :
        bomb,graph = find_bomb(graph)
        init_flag = True
        continue
    
    time = t%2
    # print(t,time)
    if time == 0:
        graph = full_bomb()
    elif time == 1 :
        graph = b_bomb(bomb)
        bomb,graph = find_bomb(graph)

for p in range(r):
    print(''.join(graph[p]))

