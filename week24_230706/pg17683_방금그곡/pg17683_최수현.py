def solution(m, musicinfos):
    answer = []
    for string in musicinfos:
        s, e, title, music_s = string.split(',')
        # 시간 계산
        s_h, s_m = map(int, s.split(':'))
        e_h, e_m = map(int, e.split(':'))
        run = (e_h - s_h) * 60 + e_m - s_m
        
        # 음악을 list로 바꾸기
        i = 0
        music = []
        while i < len(music_s):
            if music_s[i] == '#':
                music[-1] += '#'
            else:
                music.append(music_s[i])
            i += 1
        
        # 재생 시간동안의 음악 만들기
        run_music = music * (run//len(music)) + music[:run%len(music)]

        # m과 일치하면 제목과 재생시간 tuple로 저장
        l = len(m.replace('#', ''))
        for j in range(len(run_music)-l+1):
            if ''.join(run_music[j:j+l]) == m:
                answer.append((title, run))
        
    if answer:
        # 재생시간 긴 순으로 정렬 후 첫번째 항목 반환
        answer.sort(key=lambda x: x[1], reverse=True)
        return answer[0][0]
    else:
        return '(None)'