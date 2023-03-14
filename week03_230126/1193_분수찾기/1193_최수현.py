x = int(input())
grow_n = turn = 1

while x - (grow_n) > 0:
    x -= grow_n
    grow_n += 1
    turn += 1

other_n = 1
for i in range(x-1):
    other_n += 1
    grow_n -= 1

if turn & 1:
    print(f'{grow_n}/{other_n}')
else:
    print(f'{other_n}/{grow_n}')