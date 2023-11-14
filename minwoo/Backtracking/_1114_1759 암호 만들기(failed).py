# 4 6

# a t c i s w

l, c = map(int, input().split())
pw = [input().split()]
pw.sort()
answer = []  # 중복 방지 체크로 활용도 가능함.
aeiou = ['a', 'e', 'i', 'o', 'u']


#  암호 조건

#  1. 서로 달라야 함 ( 중복 불허 ) -> 지난 문제처럼 dup을 쓰자. -> pw[i] in dup?
#  2. 최소 한 개의 모음
#  3. 최소 두 개의 자음
#  4. 그리고 사전순 배열 abcdef...xyz  -> 정렬 ㄱ

#  .. 그래서, l은 3이상

def expect_pw(start):
    if len(answer) == l:
        print(*answer)
        return
    for i in range(start, l):


