# 메모리 31256 KB, 시간 40 ms
import itertools
import sys
input = sys.stdin.readline

def throw_ball(num, target):
    strike = 0
    ball = 0
    for i in range(3):
        if num[i] == target[i]:
            strike += 1
        elif num[i] in target:
            ball += 1
    return (strike, ball)

n = int(input())
answer = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0

# 3의 길이로 숫자 조합
for number in itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3):
    for t, s, b in answer:
        # 리턴값과 다른 경우 break
        if (s, b) != throw_ball(number, str(t)):
            break
    # 모두 통과 시 +1
    else:
        cnt += 1

print(cnt)
