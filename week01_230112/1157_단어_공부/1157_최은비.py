# 코드 작성 아이디어
# 1. 단어를 입력 받고 비교하기 편하게 대문자로 변경
# 2. 알파벳 중복 횟수 체크를 위한 딕셔너리 생성
# 3. 문자열 순회하면서 딕셔너리에 없는 문자열이면(등장하지 않은 문자열이면) key로 추가하고 등장횟수 1 추가
# 4. 딕셔너리에 있는 문자면(등장했던 문자면) 등장횟수 1씩 더하기
# 5. 딕셔너리 순회하면서 최대값 찾고 그에 해당하는 알파벳 출력, 최댓값이 중복이면 ? 출력

### 1157

word = input()
word = word.upper()
alph = {}
max = 0

for char in word:
    if char not in alph:
        alph[char] = 1
    elif char in alph:
        alph[char] += 1

for char in alph:
    if max < alph[char]:
        max = alph[char]
        max_char = char
    elif max == alph[char]:
        max_char = "?"

print(max_char)