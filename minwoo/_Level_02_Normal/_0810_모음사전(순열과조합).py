# A AA AAA AAAA AAAAA AAAAE AAAAI ... UUUUU

# 일단 완탐인건 알겠다. 5 ** 5 니까 그렇게 크지 않음.
# 카운트를 하는데
# ...?
# 길이 1~5개일때 모든 조합을 사전에 넣고
# 사전순 정렬을 한 다음
# 인덱스 + 1을 출력하면 될거 같은데
# 조합, 순열이 아직도 기억이 잘 안난다...

# https://latte-is-horse.tistory.com/217


from itertools import product
def solution(word):
    alp = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        dictionary.extend(list(map(''.join, product(alp, repeat=i))))

    dictionary.sort()
    return dictionary.index(word) + 1

