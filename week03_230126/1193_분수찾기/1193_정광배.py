# 1193 분수찾기

x = int(input()) # x 번째 분수 찾기
i = s = 0
while True:
    i += 1 # i 번째 줄 # 분모+분자 = i+1 
    s += i # s 번째 수는 i번째 줄 끝에 있음
    if x <= s:
        break
# x는 s에서 s-x 만큼 떨어져있다
if i % 2 == 0: # 짝수 번째 줄 # 분모 작아짐(i~ ) # 분자 커짐(1~)
    print(f'{i-s+x}/{s-x+1}') # 분자= i-(s-x) # 분모= i+1 -(분자)
else: # 홀수 번째 줄
    print(f'{s-x+1}/{i-s+x}') # 분자= i+1-(분모)  # 분모= i-(s-x)