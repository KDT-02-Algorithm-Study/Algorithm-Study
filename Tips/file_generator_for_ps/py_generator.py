# 개인이 문제를 풀때 py파일과 입력예시를 가져오기 위한 generator입니다.
# 파일 이름이나 내용을 커스텀하셔도 됩니다.
# 자신이 문제푸는 폴더에서 실행해주세요.

import requests, re
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# py파일 이름 # 커스터마이징
def get_py_name():
    py_name = f'{p_num}_{title_}.py'
    return py_name

# py파일 내용 # 커스터마이징
def get_content():
    py_content = (
f'''# https://www.acmicpc.net/problem/{p_num}
# {p_num} {title}
import sys
sys.stdin = open("{input_file}", "r")

''')
    return py_content

# input파일 이름 # 커스터마이징
def get_input_name():
    input_name = (f'input_{p_num}.txt')
    return input_name


BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_END = '\033[0m'

# main
# 여러 문제 풀때를 위해 while씀(필요없다면 삭제)
while True:
    p_num = input('>>> 문제 번호를 입력하세요. (입력이 없거나 0 입력시 종료)\n> ')

    # 입력이 없거나 0 입력시 종료
    if p_num == '' or p_num == '0' :
        break
    
    # 제목과 입력 가져오기
    url = f"https://www.acmicpc.net/problem/{p_num}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    try:
        title = soup.find('span', {'id': 'problem_title'}).text.strip()
    except:
        print(BRIGHT_RED+'== 해당 문제가 없습니다. =='+BRIGHT_END)
        continue
    input_ex = soup.find('pre', {'id': 'sample-input-1'}).text

    # re라이브러리를 사용하여 파일명으로 불가능한 문자와 공백을 '_'로 바꿔줌(정규표현식)
    title_ = re.sub(r'[\\/*:?"<>| ]', '_', title)

    py_file = get_py_name()
    input_file = get_input_name()

    # .py 생성
    # 이미 파일이 존재하면 덮어쓰기 방지
    flag = 0
    try:
        with open(py_file, 'x', encoding='utf-8') as f:
            f.write(get_content())
    except:
        print(BRIGHT_RED+'== 이미 py파일이 존재하므로 input.txt만 생성합니다. =='+BRIGHT_END)
        flag = 1

    # input.txt 생성
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(input_ex)
    
    # console 출력
    if flag:
        print(BRIGHT_GREEN+f'++ {input_file} ++'+BRIGHT_END)
    else:
        print(BRIGHT_GREEN+f'++ {py_file} ++'+BRIGHT_END)
        print(BRIGHT_GREEN+f'++ {input_file} ++'+BRIGHT_END)