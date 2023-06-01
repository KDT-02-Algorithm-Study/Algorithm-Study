# 11478 서로 다른 부분 문자열의 개수
# 31256KB / 248ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

str_list = input().rstrip()+'0'
ss,res = 0,0 
for s_len in range(len(str_list)-1,0,-1):
    ss += 1
    str_set = []
    for s in range(s_len):
        str_set.append(str_list[s:s+ss])
    str_set = set(str_set)
    res += len(str_set)

print(res)     
