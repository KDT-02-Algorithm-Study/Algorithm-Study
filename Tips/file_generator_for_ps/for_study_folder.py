# 스터디 폴더를 만들기 위한 generator입니다.
# '문제번호_이름.py'파일을 자동으로 만들어줍니다.
# name 부분을 자신의 이름으로 하드코딩으로 사용하셔도 됩니다.
# 스터디 폴더에서 실행해 주세요.

import requests, re, os
import datetime as dt
from datetime import datetime as dtdt
from bs4 import BeautifulSoup
dttd = dt.timedelta
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

START = dtdt(2023,1,12)
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_END = '\033[0m'

# 날짜 계산
def get_date():
    td = dtdt.today()
    tw = td.weekday()
    tw = (3-tw)//1%7
    td += dttd(days=tw)
    w = int(((td-START).total_seconds()/86400)//7+1)
    d = td.strftime('%y%m%d')
    
    if w < 10:
        w = '0'+str(w)

    return d, w

# 날짜 계산
DATE, WEEK= get_date()

# 날짜 폴더 생성
try:
    os.mkdir(f'week{WEEK}_{DATE}')
except:
    pass

print(BRIGHT_GREEN+f'create week{WEEK}_{DATE}'+BRIGHT_END)

# 여러 문제 만들 때를 위해 while씀(필요없다면 삭제)
while True:
    p_num = input('>>> 문제 번호를 입력하세요. (입력이 없거나 0 입력시 종료)\n> ')

    # 입력이 없거나 0 입력시 종료
    if p_num == '' or p_num == '0' :
        break
    
    # 제목 가져오기
    url = f"https://www.acmicpc.net/problem/{p_num}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    try:
        title = soup.find('span', {'id': 'problem_title'}).text.strip()
    except:
        print(BRIGHT_RED+'== 해당 문제가 없습니다. =='+BRIGHT_END)
        continue

    # re라이브러리를 사용하여 파일명으로 불가능한 문자와 공백을 '_'로 바꿔줌(정규표현식)
    title_ = re.sub(r'[\\/*:?"<>| ]', '_', title)

    fd = f'week{WEEK}_{DATE}/{p_num}_{title_}' # 폴더 이름

    # 폴더 생성
    try:
        os.mkdir(fd)
    except:
        print(BRIGHT_RED+'== 이미 폴더가 존재합니다. =='+BRIGHT_END)

    # 임시파일 생성
    with open(f'{fd}/create_folder.md', 'w', encoding='utf-8') as f:
        f.write('폴더 생성을 위한 임시 파일')
    print(BRIGHT_BLUE+fd+BRIGHT_END)
    print(BRIGHT_BLUE+'++ 임시파일 ++'+BRIGHT_END)