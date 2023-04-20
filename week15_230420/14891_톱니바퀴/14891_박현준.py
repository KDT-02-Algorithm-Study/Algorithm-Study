# 34268 KB / 92 ms

from collections import deque
gear = [deque([int(x) for x in input()])  for _ in range(4)]
K = int(input())
for _ in range(K):
    index, dir = map(int, input().split())
    index -= 1

    left = gear[index][6]
    left_dir = dir

    right = gear[index][2]
    right_dir = dir

    gear[index].rotate(dir)

    for i in range(index-1, -1, -1):
        if gear[i][2] != left:
            left = gear[i][6]
            gear[i].rotate(left_dir * (-1))
            left_dir *= (-1)
        else:
            break
    
    for i in range(index+1, 4):
        if gear[i][6] != right:
            right = gear[i][2]
            gear[i].rotate(right_dir * (-1))
            right_dir *= (-1)
        else:
            break
        
res = 0
score = 1
for i in gear:
    if i[0] == 1:
        res += score
    score *= 2
print(res)