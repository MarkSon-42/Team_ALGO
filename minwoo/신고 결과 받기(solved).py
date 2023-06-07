
# 춡처 : https://tonight-study.tistory.com/139
def solution(id_list, report, k):
    # 딕셔너리를 2개 생성. 0으로 초기화. id_list의 각 요소를 key로 사용
    id = {i:0 for i in id_list}  #
    mail = {i:0 for i in id_list}  # 해당 사용자에게 보내진 메일의 횟수를 담을 예정

    report = list(set(report))  # 신고 리스트에서 중복 제거후 다시 리스트로 변환

    r = []  # 신고 내용을 임시로 저장할 용도의 빈 리스트 생성

    for v in report:  # report 리스트를 반복하면서 각 신고 내용을 처리
        value = v.split(' ')
        id[value[1]] += 1
        r.append(value)

    for i in r:  # r 리스트를 반복하면서 메일을 보내야 할 사용자들을 판별
        if id[i[1]] >= k:
            mail[i[0]] += 1

    return list(mail.values())



# 유사한 코드

def solution2(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer