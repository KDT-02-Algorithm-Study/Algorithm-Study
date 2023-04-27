# 에디터 https://www.acmicpc.net/problem/1406
# 41948KB / 348ms
import sys
from collections import deque

input = sys.stdin.readline

n = input().strip()
m = int(input())
# 문장 맨 뒤에 커서가 있으므로 커서 오른쪽엔 아무것도 없음
left = deque(list(n))
right = deque([])

for _ in range(m):
    cmd = list(input().split())
    
    if cmd[0] == 'L':
        if not left:
            continue
        else:
            # 커서를 왼쪽으로 옮김 = 커서 왼쪽 맨 뒤에 있는 문자 하나를 커서 오른쪽 맨 앞으로 옮김
            tmp = left.pop()
            right.appendleft(tmp)

    elif cmd[0] == 'D':
        if not right:
            continue
        else:
            # 커서를 오른쪽으로 옮김 = 커서 오른쪽 맨 앞에 있는 문자 하나를 커서 왼쪽 맨 뒤로 옮김
            tmp = right.popleft()
            left.append(tmp)

    elif cmd[0] == 'B':
        if not left:
            continue
        else:
            left.pop()

    else:
        left.append(cmd[1])


print(''.join(left) + ''.join(right))