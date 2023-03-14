# 16953 A → B
# 31256 KB / 52 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 1
def cal (num1,num2):
    #print('시작', num1,num2)
    global cnt 
    if num1 == num2 :
        #print('끝', num1,num2)
        print(cnt)
        return 
    if num1 > num2 :
        #print('끝', num1,num2)
        print(-1)
        return

    if num2 % 10 == 1 :  
        cnt += 1 
        num4 = num2//10  # (str(num2))[0:len(str(num2))-1]
        #print('빼기', num1,num4)
        cal(num1,num4)
        
    elif num2 % 2 == 0 : 
        cnt += 1
        num5 = num2 // 2
        #print('나누기', num1,num5)
        cal(num1,num5)
    
    else :
        #print('끝', num1,num2)
        print(-1)
        return


cal(a,b)

## BFS 참고 
from collections import deque
a,b = map(int,input().split())
q = deque()
q.append((a,1))
r = 0

while(q):
    n,t = q.popleft()
    if n > b:
        continue
    if n == b:
        print(t)
        break
    q.append((int(str(n)+"1"),t+1))
    q.append((n*2,t+1))
else:
    print(-1)

# https://my-coding-notes.tistory.com/210