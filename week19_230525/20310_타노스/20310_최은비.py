# 타노스 https://www.acmicpc.net/problem/20310
# 31256KB / 48ms

import sys
input = sys.stdin.readline

s = list(input().strip())
cnt_zero = 0
cnt_one = 0

for i in s:
    if i == '0':
        cnt_zero += 1
    else:
        cnt_one += 1

# 0과 1 개수를 절반으로 줄이기
cnt_zero //= 2
cnt_one //= 2
idx = 0

# 사전순으로 가장 빠른 걸 찾으려면 1은 최대한 뒤에 위치해야 함
# -> 앞에서부터 1이 나오면 없애기
while cnt_one > 0:
    if cnt_one and s[idx] == '1':
        s.pop(idx)
        cnt_one -= 1
        idx = 0
    else:
        idx += 1

s = s[::-1]
idx = 0

# 반대로 0은 최대한 앞에 있어야 함
# -> 현재 문자열을 뒤집에서 뒤에서부터 0이 나오면 없애기
while cnt_zero > 0:
    if cnt_zero and s[idx] == '0':
        s.pop(idx)
        cnt_zero -= 1
        idx = 0
    else:
        idx += 1

print(''.join(s[::-1]))