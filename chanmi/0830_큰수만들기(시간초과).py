from itertools import combinations

def solution(number, k):
    # string 형태의 문자열을 하나씩 뜯어서 리스트에 넣음
    # combinations을 쓰기 위한 작업
    number_list = list(number)
    
    # Combinations을 이용해 리스트 생성
    greedy_list = list(combinations(number_list, len(number) - k))
    
    # 하나씩 확인해가며 최대값 찾기
    max_number = -100
    
    for item in greedy_list:
        test_number = int(''.join(item))
        if test_number > max_number:
            max_number = test_number
            
    return str(max_number)