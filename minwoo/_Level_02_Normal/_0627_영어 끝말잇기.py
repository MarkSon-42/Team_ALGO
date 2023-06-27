# 탈락자와 몇번째 만에 찰락하는지 두가지 값을 리턴

# 문자열의 끝 글자 ~ 첫글자 만 보면 된다

# https://yuseungyeon.tistory.com/21

def solution(n, words):
    answer = [0, 0]
    word = [words[0]]

    for i in range(1, len(words)):
        if words[i] not in word:
            if words[i][0] == word[-1][-1]:
                word.append(words[i])
            else:
                answer = [i % n + 1, i // n + 1]
                break
        else:
            answer = [i % n + 1, i // n + 1]
            break

    return answer