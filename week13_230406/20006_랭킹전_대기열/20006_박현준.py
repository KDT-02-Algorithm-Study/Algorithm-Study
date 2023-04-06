# 31256 KB / 56 ms

p, m = map(int, input().split())
player = []
room = []
for i in range(p):
    level, name = input().split()
    level = int(level)
    if i == 0:
        room.append([(level, name)])
        continue
    enter = False
    for r in room:
        if (len(r) < m) and r[0][0] - 10 <= level <= r[0][0] + 10:
            r.append((level, name))
            enter = True
            break
    if enter == False:
        room.append([(level, name)])

for i in range(len(room)):
    if len(room[i]) == m:
        print('Started!')
        rm = sorted(room[i], key=lambda x:x[1])
        for r in rm:
            print(*r)
    else:
        print('Waiting!')
        rm = sorted(room[i], key=lambda x:x[1])
        for r in rm:
            print(*r)