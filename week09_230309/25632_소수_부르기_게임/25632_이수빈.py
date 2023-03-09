# 25632 소수 부르기 게임
# 31256 KB / 128 ms
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a,b = map(int,input().split())
c,d = map(int,input().split())
yt_num,yj_num = [],[]

# 용진이의 소수
for i in range(a,b+1):
    st_flag = True
    for ii in range(2,i):
        if i % ii == 0 :
            st_flag = False
    if st_flag == True :
        yt_num.append(i)

# 유진이의 소수
for j in range(c,d+1):
    st_flag = True
    for jj in range(2,j):
        if j % jj == 0 :
            st_flag = False
    if st_flag == True:
        yj_num.append(j)
# 겹치는게 있는지 
ruq = []
for k in yt_num:
    if k in yj_num:
        ruq.append(k)

# 겹치는게 있다면 
if len(ruq) != 0 :
    # 지우고
    for u in ruq :
        yj_num.remove(u)
        yt_num.remove(u)

    # 남아 있는 갯수가 같으면
    if len(yj_num) == len(yt_num):
        # 겹치는 애의 수가 짝홀인지 구분
        if len(ruq)%2 != 0 :
            print('yt')
        else : print('yj')

    # 남아 있는 갯수가 다르면
    else : 
        # 더 긴 애를 선택
        if len(yj_num)<len(yt_num):
            print('yt')
        else : print('yj')

elif len(ruq) == 0 : # 겹치는 애가 없을 시
    if len(yj_num)<len(yt_num): print('yt')
    elif len(yj_num)>len(yt_num): print('yj') 
    else : print('yj')

        