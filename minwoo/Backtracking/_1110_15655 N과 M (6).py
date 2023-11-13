n, m = map(int, input().split())
arr = list(map(int, input().split()))
isduplicated = []

arr.sort()

def print_answer():
    for elem in isduplicated:
        print(elem, end=" ")
    print()
    return

def choose(start):
    if len(isduplicated) == m:
        print_answer()
        return
    for i in range(start, n):
        if arr[i] in isduplicated:
            continue
        isduplicated.append(arr[i])
        choose(i)
        isduplicated.pop()
    return

choose(0)