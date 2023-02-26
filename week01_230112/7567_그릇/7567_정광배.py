# 7567 그릇

data = input()

temp = data[0]
count = 10

for dish in data[1:]:
    if temp == dish:
        count += 5
    else:
        count += 10
    temp = dish

print(count)