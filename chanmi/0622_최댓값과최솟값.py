def solution(s):
    # 공백을 기준으로 String 문자를 나누어 리스트로 저장
    number_list = s.split(' ')
    
    # 문자열 형태의 값을 정수형으로 저장
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])
    
    # 내장 함수를 통해 최댓값과 최솟값 찾기
    min_num = min(number_list)
    max_num = max(number_list)
    answer = str(min_num) + ' ' + str(max_num)
    return answer