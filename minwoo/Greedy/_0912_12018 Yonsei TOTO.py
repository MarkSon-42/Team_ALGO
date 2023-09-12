#

n, m = map(int, input().split())
cnt = 0
for i in range(n):
    p, l = map(int, input().split())
    m = list(map(int, input().split()))
    m = sorted(m)
    if p < l:
        cnt += 1
    else:
        pass

    #  어려운데.
    #  https://airzinc.tistory.com/entry/%EB%B0%B1%EC%A4%80-12018-Yonsei-TOTO-%ED%8C%8C%EC%9D%B4%EC%8D%AC?category=964378
    #  짧은 풀이 ( 아직 이해 못함 )



