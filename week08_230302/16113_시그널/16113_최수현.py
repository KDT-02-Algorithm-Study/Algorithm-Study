# 메모리 31256 KB, 시간 60 ms
import sys
intput = sys.stdin.readline

n = int(input())
# 가로 길이
l = n // 5
signal = input().rstrip()

# 인덱스 0부터 시작
x = 0
while x < l:
    # 숫자라면 첫 칸은 모두 #이므로 .인 경우 다음 인덱스로 이동
    if signal[x] == '.':
        x += 1
        continue
    
    # 1
    is_one = False
    if x == l - 1:
        for i in range(5):
            if signal[i*l + x] != '#':
                break
        else:
            is_one = True
    else:
        for i in range(5):
            if signal[i*l + x] != '#' or signal[i*l + x+1] != '.':
                break
        else:
            is_one = True
    
    if is_one:
        print(1, end='')
        x += 2
        continue
    
    # 1이 아닌 경우 인덱스범위 조건
    if x > l - 3:
        break
    
    # 4가 아닌 조건
    if signal[x] == signal[x+1] == signal[x+2] == '#':
        # 0 8 9
        if signal[l+x] == signal[l+x+2] == '#' and signal[l+x+1] == '.':
            if signal[2*l + x+1] == '.':
                print(0, end='')
            elif signal[3*l + x] == '#':
                print(8, end='')
            else:
                print(9, end='')
        # 2 3 7
        elif signal[l+x] == signal[l+x+1] == '.' and signal[l+x+2] == '#':
            if signal[2*l + x] == '.':
                print(7, end='')
            elif signal[3*l + x] == '#':
                print(2, end='')
            else:
                print(3, end='')
        # 5 6
        else:
            if signal[3*l + x] == '#':
                print(6, end='')
            else:
                print(5, end='')
    else:
        print(4, end='')
    
    x += 4