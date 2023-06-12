# 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.

# k번 이상 신고된 유저는 게시판 이용이 정지되며,

# 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.

# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return

# report length 200,000

# 일단은 신고 누적 횟수부터 알아내서 정지 대상부터 추리자..

# 신고한사람과 신고당한사람 -> 여기서 공백을 기준으로 신고당한사람만 추리고 싶은데 어떻게 하나..? 슬라이스 혹은 딕셔너리 써야 할거 같은데
# 최대길이 200,000이라 복잡도를 생각해야 한다.

from collections import Counter


def solution(id_list, report, k):
    answer = []
    blocked = []
    report = list(set(report))  # 중복 신고를 처리하기 위해서 set(), 그리고 매개변수 타입에 맞게 list로 다시 바꿔주기 까지.
    for s in report:
        for i in range(len(s)):
            if s[i] == ' ':
                s = s[i + 1:]
                blocked.append(s)
                break  # 정지자들 축출 성공
                # 동일 유저에 대한 신고횟수는 어떻게 처리?
                # 처음부터 set()을 하면 되나? 문자열에도 가능? -> 가능.

    # 이제 k 이상인 요소만 남기자. -> lib Counter를 써보자.
    counter = Counter(blocked)
    print(counter)

    return answer