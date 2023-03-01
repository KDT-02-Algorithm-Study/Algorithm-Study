# 7567

plates = input()
height = 0

for i in range(len(plates)):
    if i < len(plates)-1:
        if plates[i] == plates[i+1]:
            height += 5
        else:
            height += 10

print(height + 10)