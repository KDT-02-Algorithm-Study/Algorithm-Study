# 10157 자리배정
# KB / ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

C,R = map(int,input().split())

my_seat = int(input())

#좌석을 줄 수 없는 경우 
if my_seat > C*R :
    print(0)
    exit()

#4방향 
dx = [0,1,0,-1]
dy = [-1,0,1,0]

#그리드 만들기 
grid = [[0]*C for _ in range(R)]
direction = x= y = 0

#행렬 돌면서 
for seat in range(1,C*R+1) :
    #내자리면 끝내기 
    if seat == my_seat:
        print(y+1,x+1)
        break
    else :
        #표시하고 
        grid[x][y] = seat
        #앞으로 전진 
        x += dx[direction]
        y += dy[direction]

        if x<0 or y<0 or x>=R or y>=C or grid[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            #범위 벗어나면 뒤로 뺐다가 방향 바꿔서 전진 
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]

