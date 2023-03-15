# 메모리 31256 KB, 시간 72 ms
import sys
input = sys.stdin.readline

def switch(t):
    if len(t) == l:
        if t == S:
            possible.append(1)
        return
    
    # 끝이 A인 경우 A를 떼고 재귀함수
    if t[-1] == 'A':
        switch(t[:len(t)-1])
    # 앞이 B인 경우 B를 떼고 뒤집어서 재귀함수
    if t[0] == 'B':
        switch(t[len(t)-1:0:-1])

S = input().rstrip()
T = input().rstrip()
l = len(S)
possible = []
switch(T)
print(1 if possible else 0)