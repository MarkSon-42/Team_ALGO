import sys
from collections import Counter

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 단축키의 개수
N = int(input())
input_list = [""] * N
shortcut = {}
shortcut_list = []

for i in range(N):
    input_list[i] = input()
    if '\n' in input_list[i]:
        input_list[i] = input_list[i].replace('\n', '')
    word_list = input_list[i].split()

    shortcut_find = False
    for j in range(len(word_list)):
        check_word = word_list[j][0]
        # 없는 단축키인 경우
        if check_word.upper() not in shortcut:
            word_list[j] = "[" + check_word + "]" + word_list[j][1:]
            sentence = ' '.join(word_list)
            shortcut[check_word.upper()] = sentence
            if '\n' in sentence:
                sentence = sentence.remove('\n')
            shortcut_list.append(check_word.upper())
            shortcut_find = True
            break
        # 이미 있는 경우
        else:
            continue

    is_word_in = True
    # 단어들 첫 글자가 이미 단축키에 등록된 경우
    if shortcut_find == False:
        # 스페이스 지우기
        char_list = list(input_list[i])
        is_word_in = False
        for k in range(len(char_list)):
            check_word = char_list[k]
            # 스페이스 있는 경우 넘김
            if check_word == " ":
                continue

            # 이미 등록된 단축키는 넘김
            elif check_word.upper() in shortcut:
                continue

            # 없을 경우 추가
            elif check_word.upper() not in shortcut:
                sentence = ''.join(char_list[:k]) + "[" + check_word + "]" + ''.join(char_list[k + 1:])
                shortcut[check_word.upper()] = sentence
                shortcut_list.append(check_word.upper())
                is_word_in = True
                break

    # 아예 없는 경우
    if is_word_in == False:
        shortcut[input_list[i]] = input_list[i]
        shortcut_list.append(input_list[i])

for word in shortcut_list:
    print(shortcut[word])