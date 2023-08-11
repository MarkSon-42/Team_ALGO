# 하드웨어의 가격이 저렴해지길 기도하는 코드
# 복잡도 고려하는 문제가 아니라면 이렇게라도 통과는 해야함...
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U', '']
    tmp = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i + j + k + l + m
                        if w not in tmp: tmp.append(w)

    tmp.sort()
    return tmp.index(word)



#     alpha = ['A', 'E', 'I', 'O', 'U', '']에 공백이 추가되어있는 이유
# gpt : 그런데 만약 빈 문자열('')이 alpha 리스트에 없다면,

# 마지막 위치에 있는 단어 "UUUUU"를 생성할 수 없습니다. 빈 문자열은 길이가 0인 단어를 나타내며,
# 모든 길이의 단어를 생성할 수 있는 조합을 표현합니다.

