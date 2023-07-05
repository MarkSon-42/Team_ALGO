def solution(citations):
    
    # 인용된 횟수를 저장하는 dict 변수
    count = {}
    
    # 최대 인용 횟수 찾기
    number_max = max(citations)
    
    # citations와 인용 횟수를 0부터 number_max까지 비교하여 인용횟수를 저장하는 dict 생성
    for i in range(number_max):
        for item in citations:
            if item >= i:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
    
    # 인용 횟수를 내림차순 정렬
    count = sorted(count.items(), key = lambda item : item[1], reverse=True)
    
    # h번 이상 인용된 논문이 h편 이상일 때의 최대 h값 찾기
    find_max = 0
    for item in count:
        if item[0] <= item[1]:
             find_max = item[0]
    return find_max