#  https://codingwonny.tistory.com/304

n = int(input())

# 단축키로 지정되었다고 표시하기 위해 flag 변수를 사용하였다.
# 이때 주의해야할 점은 단축키를 지정할 때 대소문자 구분을 하지 않는다고 했으므로
# 모두 대문자로 단축키 리스트에 저장

exist = []
for _ in range(n):
    words = list(input().split())

    flag = False
    for i in range(len(words)):
        if words[i][0].upper() not in exist:
            exist.append(words[i][0].upper())
            flag = True
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            print(' '.join(words))
            break

    if not flag:
        for i in range(len(words)):
            check = False
            for j in range(len(words[i])):
                if words[i][j].upper() not in exist:
                    exist.append(words[i][j].upper())
                    flag = True
                    check = True
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                    print(' '.join(words))
                    break
            if check: break

    if not flag:
        print(' '.join(words))