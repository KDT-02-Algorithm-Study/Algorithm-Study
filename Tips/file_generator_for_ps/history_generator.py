# 아무 폴더에서 실행 후 터미널 출력 복사

from requests import get
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

week = input('>>> 몇 번째 주 인가요? (입력이 없거나 0 입력시 종료)\n> ')

# 입력이 없거나 0 입력시 종료
if week == '' or week == '0':
    exit()

table = f'🏃week{week}\n\n|번호|제목|\n|:-:|:-:|\n'
p_li = set()
while True:
    print('추가된 번호: ',end='')
    for num, title in sorted(p_li):
        print(num,end=' ')
    print()
    p_num = int(input('>>> 문제 번호를 입력하세요. (입력이 없거나 0 입력시 출력 후 종료)\n> '))

    # 입력이 없거나 0 입력시 출력 후 종료
    if p_num == '' or p_num == 0:
        for num, title in sorted(p_li):
            table += f'|{num}|[{title}](https://www.acmicpc.net/problem/{num})|\n'
        print()
        print(table)
        input('\nEnter 입력시 종료...')
        break
    
    # 제목 가져오기
    url = f"https://www.acmicpc.net/problem/{p_num}"
    res = get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    try:
        p_title = soup.find('span', {'id': 'problem_title'}).text.strip()
    except:
        print('== 해당 문제가 없습니다. ==')
        continue
    
    p_li.add((p_num, p_title))

    # 6개면 출력 후 종료
    if len(p_li) == 6:
        for num, title in sorted(p_li):
            table += f'|{num}|[{title}](https://www.acmicpc.net/problem/{num})|\n'
        print()
        print(table)
        input('\nEnter 입력시 종료...')
        break