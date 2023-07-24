# https://velog.io/@godiva7319/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-1%EC%B0%A8-%EB%89%B4%EC%8A%A4-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81-Python

from collections import Counter
def solution(str1, str2):
    # 1. 가장 먼저 해야 할 일은 매개변수인 str1과 str2의 전처리
    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []
    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for i in range(len(str2_low) - 1):
        if str2_low[i].isalpha() and str2_low[i + 1].isalpha():
            str2_lst.append(str2_low[i] + str2_low[i + 1])

    # Counter() : 각각의 리스트는 해당 원소값을 key값으로 하고, 원소의 갯수를 value값으로 하는 dictionary 형태의 구조를 반환

    counter_01 = Counter(str1_lst)
    counter_02 = Counter(str2_lst)

    # elements()를 이용해서 원소값만을 추출하기
    inter = list((counter_01 & counter_02).elements())
    union = list((counter_01 | counter_02).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)