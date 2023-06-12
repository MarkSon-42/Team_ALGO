# 날짜문제, 윤년문제 -> A 전부 최소단위(일)로 바꿔버리기
def solution(today, terms, privacies):
    answer = []
    y, m, d = today.split('.') # 연,월,일을 '.'로 구분하여 각각 할당
    today = int(y)*12*28 + int(m)*28 + int(d) # 예) 2021.05.02 -> 6863일

    # 약관 종류를 딕셔너리 형태로 바꿔줌 (약관 종류:유효기간(일 단위))


    terms = {i[:1] : int(i[2:]) * 28 for i in terms}

    new_terms = {}  # 빈 사전을 생성하여 새로운 항목을 저장할 변수를 초기화합니다.

    for i in terms:  # terms 사전의 각 항목에 대해 반복합니다.
        key = i[:1]  # 현재 항목의 첫 번째 문자를 키로 사용합니다.
        value = int(i[2:]) * 28  # 현재 항목의 세 번째 문자부터 끝까지를 정수로 변환한 후 28을 곱한 값을 값으로 설정합니다.
        new_terms[key] = value  # 새로운 항목을 new_terms 사전에 추가합니다.
    terms = new_terms  # new_terms 사전을 terms 사전으로 업데이트합니다.

    # terms를 dict로 바꿔주는데
    # value 안에 반복문을 통해서 일단위로 통일함.

    # p : privacies 원소(수집일자)를 '일'단위로 치환
    # c : 약관종류
    for i,p in enumerate(privacies):
        y,m,d = p.split('.')
        d,c = d.split()  #  d = 02  c = A
        p = int(y)*12*28 + int(m)*28 + int(d)

        if p+terms[c] <= today:
            answer.append(i+1) # (수집일자 + 약관종류에 따른 일자)가 오늘을 넘지 않으면 정답(인덱스+1)에 추가 (번호가 1부터 시작하니까)

    return answer
