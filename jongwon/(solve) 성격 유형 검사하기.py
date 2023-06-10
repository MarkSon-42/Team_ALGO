def solution(survey, choices):
    indicators = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0} # 각 지표 점수를 딕셔너리로 0으로 시작
    choices_dict = {1:3, 2:2, 3:1, 4:0, 5: 1, 6:2, 7:3} # 선택지에 대한 점수 딕셔너리
    
    for i in range(len(survey)):
        if choices[i] > 4: # 4보다 크면 후자의 성격 유형에 점수 더해주기
            indicators[survey[i][1]] += choices_dict[choices[i]]
        elif choices[i] < 4: # 4보다 작으면 전자의 성격 유형에 점수 더해주기
            indicators[survey[i][0]] += choices_dict[choices[i]]
        else: # choices = 4인 경우는 0
            indicators[survey[i][0]] += 0
    
    mbti = []
    if indicators['R'] > indicators['T']:
        mbti.append('R')
    elif indicators['R'] < indicators['T']:
        mbti.append('T')
    else: # 점수가 같을 때
        mbti.append('R')
    
    if indicators['C'] > indicators['F']:
        mbti.append('C')
    elif indicators['C'] < indicators['F']:
        mbti.append('F')
    else: # 점수가 같을 때
        mbti.append('C')
        
    if indicators['J'] > indicators['M']:
        mbti.append('J')
    elif indicators['J'] < indicators['M']:
        mbti.append('M')
    else: # 점수가 같을 때
        mbti.append('J')
        
    if indicators['A'] > indicators['N']:
        mbti.append('A')
    elif indicators['A'] < indicators['N']:
        mbti.append('N')
    else: # 점수가 같을 때
        mbti.append('A')
    
    result = ''.join(mbti)
    
    return result # 결과 반환