# 114692 KB / 1004 ms

N = int(input())
tower = [int(x) for x in input().split()]

# 높은 탑을 넣을 stack
stack = []

for i in range(N):
    # 현재 탑의 높이를 cur_tower에 저장
    cur_tower = tower[i]
    while stack:
        
        # 스택에 있는 탑의 높이가 더 크면, 스택 탑의 높이 출력
        if stack[-1][1] >= cur_tower:
            print(stack[-1][0] + 1, end=' ')
            break
        
        # 아니면 스택에서 뺌
        else:
            stack.pop()
            
    # 스택에 탑이 없으면, 높은 탑이 없는것이므로 0을 출력
    if not stack:
        print(0, end=' ')
        
    # 스택에 인덱스와 탑의 높이를 쌍으로 append
    stack.append([i, tower[i]])