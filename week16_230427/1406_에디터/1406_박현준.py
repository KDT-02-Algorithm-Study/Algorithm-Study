# 41680 KB / 380 ms

import sys
left = [x for x in sys.stdin.readline().rstrip()]
right = []

N = int(input())
for _ in range(N):
    
    # 입력한 명령어 
    stdin = [x for x in sys.stdin.readline().split()]
    
    # 명령어를 담을 op 변수
    op = stdin[0]
    
    if op == 'L':
        if left:
            right.append(left.pop())
    elif op == 'D':
        if right:
            left.append(right.pop())
    elif op == 'B':
        if left:
            left.pop()
    else:
        left.append(stdin[1])
print(''.join(left + right[::-1]))