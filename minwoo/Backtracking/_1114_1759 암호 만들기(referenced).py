# 조건 2, 3을 처리실패해서 아래 블로그를 참고하였음.

# https://codinghejow.tistory.com/230

l, c = map(int, input().split())
pw = sorted(list(map(str, input().split())))

answer = []  # 중복 방지 체크로 활용도 가능함.
aeiou = ['a', 'e', 'i', 'o', 'u']

def expect_pw(cnt, idx):
    if cnt == l:
        vow, con = 0, 0    #       자음 : consonants 모음 vowels

        for i in range(l):
            if answer[i] in aeiou:
                vow += 1
            else:
                con += 1

        if vow > 0 and con > 1:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(pw[i])
        expect_pw(cnt + 1, i + 1)
        answer.pop()

expect_pw(0, 0)

# 근데 왜 list out of range..
# pw = sorted(list(map(str, input().split())))
# 매핑을 해줘야 한다
# 이유는 아직 모르겠음
# pw = sorted([input().split()])는 안됨
# 출력해보면 결과는 같은데..
