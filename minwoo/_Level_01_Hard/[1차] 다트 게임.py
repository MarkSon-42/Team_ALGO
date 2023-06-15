def solution(dartResult):
    dartResult = list(dartResult)  # 주어진 문자열을 리스트로 변환하여 처리하기 쉽게 함
    num = [[] * 3 for i in range(3)]  # 점수를 저장할 리스트 초기화
    answer = 0  # 최종 점수
    nowNum = '0'  # 현재 처리 중인 숫자
    count = 0  # 점수를 저장할 리스트의 인덱스

    for i in dartResult:  # 문자열을 한 글자씩 순회하며 처리
        if i.isdigit() == True:  # 현재 글자가 숫자인 경우
            if nowNum == '0':  # 현재 숫자가 0인 경우
                count += 1  # 새로운 점수를 저장할 리스트의 인덱스 증가
            nowNum += i  # 현재 글자를 현재 숫자에 추가
        else:  # 현재 글자가 숫자가 아닌 경우
            nowNum = int(nowNum)  # 현재 숫자를 정수로 변환

            if i.isalpha() == True or i == '#':  # 현재 글자가 알파벳 또는 #인 경우
                if i == 'S':  # Single 점수인 경우
                    nowNum **= 1  # 현재 숫자를 1제곱하여 갱신
                elif i == 'D':  # Double 점수인 경우
                    nowNum **= 2  # 현재 숫자를 2제곱하여 갱신
                elif i == 'T':  # Triple 점수인 경우
                    nowNum **= 3  # 현재 숫자를 3제곱하여 갱신
                elif i == '#':  # 현재 글자가 #인 경우
                    nowNum = -1  # 현재 숫자에 -1을 곱하여 갱신

                num[count-1].append(nowNum)  # 현재 숫자를 저장할 리스트에 추가
            else:  # 현재 글자가 숫자도 알파벳도 #이 아닌 경우
                if count == 3:  # 이미 세 개의 점수를 저장한 경우
                    num[1].append(2)  # 두 번째 리스트에 2 추가
                    num[2].append(2)  # 세 번째 리스트에 2 추가
                else:  # 아직 세 개의 점수를 저장하지 않은 경우
                    for j in range(count):  # 현재까지의 점수를 저장한 리스트 순회
                        num[j].append(2)  # 리스트에 2 추가 (보너스 처리)

            nowNum = '0'  # 현재 숫자 초기화

    for i in range(3):  # 각 리스트의 점수 계산
        resultNum = num[i][0]  # 리스트의 첫 번째 점수를 초기값으로 설정

        for j in range(len(num[i])-1):  # 나머지 점수들에 대해 반복하여 처리
            resultNum *= num[i][j+1]  # 이전 점수와 현재 점수를 곱하여 갱신

        answer += resultNum  # 최종 점수에 현재 리스트의 점수를 더함

    return answer  # 최종 점수 반환
