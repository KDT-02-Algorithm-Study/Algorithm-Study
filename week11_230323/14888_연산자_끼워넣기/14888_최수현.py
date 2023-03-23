# 31256 KB, 68 ms
import sys
input = sys.stdin.readline

def calc(total, tool, index):
    if index == n:
        result.append(total)
        return
    
    for i in range(4):
        if tool[i] != 0:
            tool[i] -= 1

            if i == 0:
                calc(total + nums[index], tool, index + 1)
            elif i == 1:
                calc(total - nums[index], tool, index + 1)
            elif i == 2:
                calc(total * nums[index], tool, index + 1)
            else:
                if total < 0:
                    calc(-1 * ((-1 * total) // nums[index]), tool, index + 1)
                else:
                    calc(total // nums[index], tool, index + 1)

            tool[i] += 1


n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
result = []
# 현재 계산결과, 연산자 개수, 다음 인덱스
calc(nums[0], operator, 1)

print(max(result))
print(min(result))