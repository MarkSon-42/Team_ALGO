import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스의 개수를 입력받습니다.
t = int(input())

# 각 테스트 케이스를 처리합니다.
for _ in range(t):
    func = input().rstrip()  # 수행할 함수를 입력받습니다.
    n = int(input())  # 배열의 길이를 입력받습니다.
    flag = 1  # 에러 발생 여부를 표시할 플래그를 초기화합니다.
    arr = input().strip()  # 배열을 입력받습니다.

    # 입력된 배열 문자열을 파싱하여 덱(queue)를 생성합니다.
    queue = deque(arr[1:-1].split(','))

    if n == 0:
        queue = deque()  # 배열 길이가 0이면 빈 큐를 생성합니다.

    R = 0  # 뒤집기 횟수를 초기화합니다.

    # 수행할 함수를 순회하며 큐를 조작합니다.
    for i in range(len(func)):
        if func[i] == 'R':
            R += 1  # R 함수가 호출되면 뒤집기 횟수 증가합니다.
        elif func[i] == 'D':
            if len(queue) == 0:
                print('error')  # 큐가 비어있는데 D 함수가 호출되면 에러를 출력합니다.
                flag = 0
                break
            else:
                if R % 2 == 0:
                    queue.popleft()  # R이 짝수번 호출되면 큐의 왼쪽에서 삭제합니다.
                else:
                    queue.pop()  # R이 홀수번 호출되면 큐의 오른쪽에서 삭제합니다.

    if flag == 0:
        continue  # 에러가 발생한 경우, 다음 테스트 케이스로 넘어갑니다.
    else:
        if R % 2 == 0:
            print('[' + ','.join(queue) + ']')  # R이 짝수번 호출된 경우, 큐를 출력합니다.
        else:
            queue.reverse()  # R이 홀수번 호출된 경우, 큐를 뒤집고 출력합니다.
            print('[' + ','.join(queue) + ']')
