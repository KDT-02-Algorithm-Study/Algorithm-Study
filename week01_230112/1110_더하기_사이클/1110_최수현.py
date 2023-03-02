origin_number = int(input())
number = origin_number
cnt = 0

while True:
    if number < 10:
        a = 0
        b = number
    else :
        a = int(str(number)[0])
        b = int(str(number)[1])

    number = int(str(b) + str((a+b)%10))
    cnt += 1
    if number == origin_number:
        break

print(cnt)