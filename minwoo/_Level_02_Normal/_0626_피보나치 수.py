def solution(n):
    fb = [0, 1]
    for i in range(2, n + 1):
        fb.append(fb[i - 1] + fb[i - 2])
        #  피보나치 수열의 규칙에 따라 이전 두 개의 수를 더하여 다음 수를 계산하고 fb 리스트에 추가
    answer = fb[-1] % 1234567
    return answer


#  피보나치 수열의 규칙 ?

#  이전 두 수를 더해서 다음 수를 생성하는 규칙을 가지며, 이를 반복하여 수열을 구성

