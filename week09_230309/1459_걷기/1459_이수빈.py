# 1459 걷기
# 31256KB / 44ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

x,y,w,s = map(int,input().split())
path = []
# 평행이동만 할 때 
path.append((x+y)*w)

# 대각선으로만 이동할 때 
# 합이 짝수일 때 -> 오로지 대각선으로만 이동할 수 있음 
if (x+y)% 2 == 0 :
    path.append(max(x,y)*s)

# 합이 홀수일 때 -> 대각선 이동 + 한 번 평행이동
else :  
    path.append((max(x,y)-1)*s+w)

# 대각선 + 평행이동 
path.append((min(x,y)*s)+((max(x,y)-min(x,y)))*w)

print(min(path))
