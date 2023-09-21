'''
문제 : 사다리 타기
링크 : https://www.acmicpc.net/problem/2469
소요시간 : 
'''
import sys
se = sys.stdin.readline
k = int(input())
n = int(input())

# -가 연속해서 주어지는 경우는 없다. 따라서, 좌우를 살폈을 떄 내가 이동할 수 있는 곳으로만 이동하면 된다.

# 그래프는 다음과 같이 구성하자.
# 1. 행이 n+2, 열이 k인 그래프
# 2. 1행엔 아스키코드로 ABCD...가 순서대로 들어가고, 마지막 행에 최종값을 저장해준다.
# 3. 최종값을 str과 비교해서 맞으면 해당 값을 return 해주자.
# 3-1. return 할 떈 ? 가 있는 행을 ''.join으로 문자열 출력해주자.

# k-1번 반복, 모든 경우의 수를 체크하자.
# for _ in range(k-1):
    