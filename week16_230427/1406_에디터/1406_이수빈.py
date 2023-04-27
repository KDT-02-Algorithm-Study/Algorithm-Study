# 1406 에디터
# 37576 KB / 316 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# append와 pop을 활용하면 o(1)의 시간 연산
# 이를 잘 활용하기 위해 stack을 사용
# 커서를 기준으로 문자열을 스택 두 개에 나누어 담는 것

left = list(input().rstrip())
right = []

for _ in range(int(input())):
    order = list(input().split())
    if order[0] == 'L' and left:
        right.append(left.pop())
    elif order[0] == 'D' and right:
        left.append(right.pop())
    elif order[0] == 'B' and left:
        left.pop()
    elif order[0] == 'P':
        left.append(order[1])
print(left,right) 
# ['y'] ['c', 'b', 'a', 'x']
# yxabc 
left.extend(reversed(right))
print(''.join(left))



# 자료구조 사용 안 했을 경우..
# 입력가능한 명령의 수는 최대 500000개
# O(n)만큼의 시간을 소요하는 insert와 remove 함수 
# 최대 길이인 100000에 최대 명령 수 500000을 곱한 숫자만큼의 연산을 진행

# 풀이 1
'''
edit = list(input().rstrip())
T = int(input())
cuser = len(edit)

for t in range(T):
    order = list(input().split())
    if order[0] == 'P' : # P일 경우
        edit.insert(cuser,order[1])
        cuser += 1 
    elif order[0] == 'L' and cuser > 0:
        cuser -= 1
    elif order[0] == 'D' and cuser < len(edit):
        cuser += 1
    elif order[0] == 'B' and cuser > 0:
        edit.pop(cuser-1)
        cuser -= 1
    else :
        continue
    
print(''.join(edit))
'''
