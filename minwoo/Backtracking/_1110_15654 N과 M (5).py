n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []
visited = [False] * (n + 1)

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()


def choose():
    if len(answer) == m:
        print_answer()
        return

    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(arr[i])
        choose()
        answer.pop()
        visited[i] = False

choose()
