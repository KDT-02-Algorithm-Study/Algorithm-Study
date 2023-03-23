# 14888 연산자 끼워넣기
# 14888 KB / 72 ms

def per(t, l):
    if l == n-1: # 연산자를 다 썼으면
        result.append(t)
        return
    
    for i in range(4):
        if oper[i]: # 연산자가 남아있으면 해당 연산에 맞게 재귀
            oper[i] -= 1 # 사용 표시
            if i == 0: # +
                per(t + a[l+1],l+1)
            elif i == 1: # -
                per(t - a[l+1],l+1)
            elif i == 2: # *
                per(t * a[l+1],l+1)
            else: # //
                if t < 0: # 음수일 때
                    per(-(-t // a[l+1]),l+1)
                else: # 양수일 때
                    per(t // a[l+1],l+1)
            oper[i] += 1


n = int(input())
a = list(map(int, input().split()))
oper = list(map(int, input().split())) # + - * //
result = []
per(a[0],0)
print(max(result), min(result), sep='\n') # 최댓값, 최솟값 출력