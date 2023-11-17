# 모든 부분 수열을 검사할 순 없고,

# 인접한 부분수열이 반드시 달라야 하게끔 백트래킹 재귀를 구현하면 될텐데

# 일단 당연히 연속된 수가 등장해선 안됨

# n 1 ~ 80

n = int(input())
answer = [0, 0, 0, 0, 0, 0, 0, 0]
elem = [1, 2, 3]
def good_numbers(x):
    if x == n:
        print(' '.join(map(str, answer)))
        return
    else:
        for i in range(2):
            if answer[i] != answer[i + 1]:
                answer.append(elem[i])
                good_numbers(x + 1)
                answer.pop()


        return

good_numbers(0)


# 해답 코드를 봤는데 아직 이걸 익힐 레벨이 아닌거 같다.

# 문자열 검사부터 다시 공부해야 할듯