import sys

input = sys.stdin.readline

n = int(input())
data = [i for i in range(1, n + 1)]

stack = list(map(int, input().split()))
result = []

while True:
    t = stack.pop()
    tmp = len(stack) - 1  # 현재 스택에서 가리키는 인덱스  len -1

    if tmp == -1:
        result.append(0)
        break

    if t > stack[tmp]:
        while True:
            tmp -= 1
            if t <= stack[tmp]:
                result.append(data[tmp])  # 현재 스택의 값보다 작은 값이 나올 때까지
                break
            if tmp == -1:
                result.append(0)  # 끝까지 찾아도 없으면 0을 추가
                break
    else:
        result.append(data[tmp])  # 현재 스택의 값이 더 크거나 같으면 추가

result.reverse()  # 출력 역순으로 해줘야함

for i in result:
    print(i, end=' ')


