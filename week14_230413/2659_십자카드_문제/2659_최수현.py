# 31256 KB / 44 ms
import sys
input = sys.stdin.readline

n = input().rstrip().replace(' ', '')
n += n  # 두개 붙이기

# 시계수 구하기
target = int(min(n[0:4], n[1:5], n[2:6], n[3:7]))
check = [False] * 10000
cnt = 0

for i in range(1111, 10000):
    if i == target:
        print(cnt + 1)
        break

    if '0' in str(i):
        continue

    if not check[i]:
        cnt += 1
        temp = str(i) * 2
        # 지금 수로 가능한 4개의 수 모두 True 처리
        for j in range(4):
            check[int(temp[j:j+4])] = True