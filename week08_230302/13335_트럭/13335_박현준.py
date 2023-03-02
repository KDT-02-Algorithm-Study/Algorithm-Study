from collections import deque
n, w, L = map(int, input().split())
queue = deque([int(x) for x in input().split()])
bridge = deque([0 for _ in range(w)])
time = 0
while queue:    
    bridge.popleft()
    if len(bridge) < w:
        if queue[0] + sum(bridge) <= L:
            bridge.append(queue.popleft())
        else:
            bridge.append(0)
    time += 1
print(time + w)