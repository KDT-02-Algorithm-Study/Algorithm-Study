K = int(input())
width = []
height = []
side = []
big_square = 1
for _ in range(6):
    dir, length = map(int, input().split())
    if dir <= 2:
        width.append(length)
        side.append(length)
    else:
        height.append(length)
        side.append(length)
big_square = max(height) * max(width)
small_square = side[(side.index(max(width))+3) % 6] * side[(side.index(max(height))+3) % 6]
print((big_square - small_square)*K)