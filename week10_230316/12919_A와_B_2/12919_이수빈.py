# 12919 A와 B 2
# 31256KB / 40ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline



def dfs(T):
  if T==S:
    return True 
  # 맨 마지막이 A라면 그냥 뒤집기만하기
  if len(T) > 1 and T[-1]=='A' and dfs(T[:-1]):
    return True
  
  # 추가하고 뒤집는 것 -> 이미 뒤집어 있기 떄문에 
  # 만약 맨 앞이 B면 뒤집었을 것 
  # B빼고 다시 뒤집어주기 
  if len(T) > 1 and T[0]=='B' and dfs(T[1:][::-1]):
    return True
  
  return False

S = input().strip()
T = input().strip()
if dfs(T):
  print(1)
else:
  print(0)