# 34144 KB / 64 ms
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

# 첫째 줄이 인덱스, 둘째 줄이 값
# 인덱스 : 0 1 2 3 4 5 6 7
# 둘째줄 : 0 3 1 1 5 5 4 6
pair_nums = [0] * (n+1)

# 둘째 줄을 딕셔너리로 개수 저장
n_cnt = {}
for i in range(n):
    a = int(input())
    pair_nums[i+1] = a
    n_cnt[a] = n_cnt.get(a, 0) + 1

# 둘째 줄에 없는 수는 그 수가 가리키는 값을 -1
second_line = n_cnt.keys()
for i in range(1, n+1):
    if i not in second_line:
        n_cnt[pair_nums[i]] -= 1

# 개수가 0 이하이면 to_delete에 추가
to_delete = deque()
for key in second_line:
    if n_cnt[key] <= 0:
        to_delete.append(key)

while to_delete:
    x = to_delete.popleft()
    if x in n_cnt:
        n_cnt.pop(x)
        # pair = x가 가리키는 값
        pair = pair_nums[x]
        if pair in n_cnt:
            n_cnt[pair] -= 1
            # x가 가리키는 값을 -1 했는데 0이하가 되면 to_delete에 추가
            if n_cnt[pair] <= 0:
                to_delete.append(pair)

print(len(n_cnt))
for k in sorted(n_cnt.keys()):
    print(k)


"""
<첫째줄>
1 2 3 4 5 6 7

둘째 줄 -> 딕셔너리로 개수 저장
{
1: 2
3: 1
4: 1
5: 2
6: 1
}
"""