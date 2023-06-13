'''
문제 : 개인정보 수집 유효기간
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3
'''

from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    
    # today를 datetime 형태로 변경해준다.
    today = datetime.strptime(today,'%Y.%m.%d')
    
    # date랑 timedelta를 쓰는데, 한 달이 28일임을 고려해야 한다.
    # 1. 약관별 유효기간을 의미하는 map을 만들어준다
    termDic = {}
    for i in terms:
        termDic[i.split()[0]] = int(i.split()[1])
    
    # 2. privacies for문을 돌면서, n개월 뒤 유효기간 만료인지 추출해준다.
    for i in range(len(privacies)):
        # 정보 수집 날짜와 약관 저장
        date = datetime.strptime(privacies[i].split()[0],'%Y.%m.%d')
        expire = termDic[privacies[i].split()[1]]
        # 2-1. 3개월 뒤면 예를들어 2020.2.19 면 2020.5.19 이렇게 변함, 따라서 하루 빼주자.
        if (date + relativedelta(months=expire)) - relativedelta(days=1) < today:
            answer.append(i+1)
        
    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])