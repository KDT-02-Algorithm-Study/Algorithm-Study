# 31256 KB / 140 ms

N = int(input())
cnt = 0

# 들어가는 차량
car_in = {}

# 나오는 차량
car_out = []

# 차량이 들어가는 순서를 저장하기 위해, 딕셔너리로 저장
for i in range(N):
    car = input()
    car_in[car] = i

# 나오는 차량을 차례로 저장
for i in range(N):
    car = input()
    car_out.append(car)


for i in range(N):
    for j in range(i+1, N):
        if car_in[car_out[i]] > car_in[car_out[j]]:
            print(car_in[car_out[i]], car_in[car_out[j]])
            cnt += 1
            break
print(cnt)

"""
one   : 1
two   : 2
three : 3
four  : 4

four
one
two
three

one   : 1 -> 2
two   : 2 -> 3
three : 3 -> 4
four  : 4 -> 1  <--

"""