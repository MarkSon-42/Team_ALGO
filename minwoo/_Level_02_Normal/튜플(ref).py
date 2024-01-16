# strip(), replace()를 적재적소에 활용할 수 있는가..
# Counter()

from collections import Counter

def solution(s):
    answer = []
    word = s.replace("{","").replace("}", "").split(",")
    count_word = Counter(word).most_common()
    for i in count_word:
        answer.append(int(i[0]))
    return answer


# 두번째 풀이

# from collections import Counter

def solution2(s):
    word_list = list(map(int, s.replace("}", "").replace("{", "").split(",")))
    count_dict = Counter(word_list).most_common()
    answer = [item[0] for item in count_dict]
    return answer

# 세번째 풀이

def solution3(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


# *** 정규식 풀이
=
import re
def solution4(s):
    answer = []
    arr = sorted(list(map(eval, re.findall("{[\d,]+}", s))))
    answer.append(list(arr[0])[0])
    for i in range(len(arr) - 1):
        answer.append(list(arr[i + 1] - arr[i])[0])
    answer = list(map(int,answer))
    return answer
