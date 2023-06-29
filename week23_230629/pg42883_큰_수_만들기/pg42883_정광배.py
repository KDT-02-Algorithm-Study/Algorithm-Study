# 큰 수 만들기
# 테스트 10 〉	통과 (140.17ms, 12.9MB)

def solution(number, k):
    stack = []
    
    # number 순회
    for now in number:
        # stack최상단이 now보다 작고, k가 남아있을 때
        # 한 자리씩 비교하기 때문에 int로 변환을 안 해도 된다.
        while stack and stack[-1] < now and k > 0:
            stack.pop()
            k -= 1 # k 감소
        stack.append(now)

    # 남은 k 처리(now가 더 작았을경우 남는다(ex. 54321, 2))
    if k > 0:
        stack = stack[:-k] # 남아있는 k만큼 뒤에서 뺌

    return ''.join(stack)