# 메모리 31256 KB, 시간 40 ms
import itertools

rome = [1, 5, 10, 50]
case_n = set()
# 중복을 포함한 조합을 리턴하는 함수
for nums in itertools.combinations_with_replacement(rome, int(input())):
    case_n.add(sum(nums))

print(len(case_n))
