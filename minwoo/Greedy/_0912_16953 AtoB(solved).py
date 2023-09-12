#
# A, B = map(int, input().split())
# cnt = 1
# for i in range(1, int(B**0.5) + 1): # 가능 연산을 고려할때 곱하기 2를 거꾸로하면 제곱근
#     if A == B:
#         break
#     if B % 2 == 0:
#         B //= 2
#         cnt += 1
#     else:
#         tmp = str(B)
#         tmp = tmp[:len(tmp)]
#         B = int(tmp)
#         cnt += 1
#
# print(cnt)
#
#


A, B = map(int, input().split())
cnt = 1
while A != B:
    cnt += 1
    tmp = B

    if B % 10 == 1:
        B //= 10 #
    elif B % 2 == 0:
        B //= 2
    # 위 두 연산을 수행했지만 값의 변화가 없을 경우,
    #
    # 무한루프에 빠지게 된 것이므로 탈출하고 -1을 출력하면 된다.
    # https://my-coding-notes.tistory.com/210
    #       V  아래 로직 위 블로그 참고함.
    if tmp == B:
        print(-1)
        break
else:
    print(cnt)