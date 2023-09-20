# 단축키를 지정하는 법

shortcut = []
answer = []
# 입력되는 문자열은 정상적인 단어만 입력되는건지..?
# 단어의 첫글자 -> 단어는 띄어쓰기로 구분됨.
# 단축키 중복에 있어 대소문자를 구분하지 않음..
n = int(input())

for _ in range(n):
    word = input()
    # 우선 단일단어만 주어지는 경우에는 바로 앞 문자를 단축키로 지정.
    if word[0] not in shortcut and ' ' not in word:
        if word[0].isupper():
            shortcut.append(word[0])
            shortcut.append(word[0].lower())
            answer.append(word[0])
        else:
            shortcut.append(word[0])
            shortcut.append(word[0].upper())
            answer.append(word[0])


    # e.g 1   ['N', 'O', 'S']
    else:
        for i in range(1, len(word)):
            if word[i - 1] == ' ' and word[i] not in shortcut:
                if word[i].isupper():
                    shortcut.append(word[0])
                    shortcut.append(word[0].lower())
                    answer.append(word[0])
                else:
                    shortcut.append(word[0])
                    shortcut.append(word[0].upper())
                    answer.append(word[0])


print(shortcut)
print(answer)
