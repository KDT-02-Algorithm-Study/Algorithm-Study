# 31256 KB, 52 ms
import sys
input = sys.stdin.readline

n = int(input())
car_input = list(input().rstrip() for _ in range(n))
car_output = list(input().rstrip() for _ in range(n))
cnt = 0

# input을 output으로 바꿔가며 추월한 차의 개수 카운트
for i in range(n):
    if car_input[i] != car_output[i]:
        car_input.remove(car_output[i])
        car_input.insert(i, car_output[i])
        cnt += 1
        
print(cnt)