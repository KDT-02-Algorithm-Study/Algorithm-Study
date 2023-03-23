# 21735 눈덩이 굴리기
# 31256 KB / 40 ms

def dfs(i, snow, time):
    if not time or i == n: # 시간을 다 쓰거나 끝에 도달할 때
        r.append(snow)
        return
    if (g:=i+1) <= n:   # 굴릴 때
        dfs(g, snow+a[g], time-1)
    if (j:=i+2) <= n:   # 점프할 때
        dfs(j,snow//2 + a[j],time-1)
    
n, m = map(int, input().split())
a = [0]+list(map(int, input().split())) # 0부터 출발하므로 [0]+ 해줌
r = []
dfs(0,1,m) # 인덱스, 눈덩이, 시간
print(max(r))