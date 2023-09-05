def findMax(start_index, items, cap):
    cur = cap
    while start_index >= 0 and cur:
        if items[start_index] > cur:
            items[start_index] -= cur
            cur = 0
        else:
            cur -= items[start_index]
            items[start_index] = 0
            while start_index >= 0 and items[start_index] == 0:
                start_index -= 1
    return start_index

def solution(cap, n, deliveries, pickups):
    i, j = n - 1, n - 1 # 배달/수거해야하는 가장 먼 곳
    while i >= 0 and deliveries[i] == 0: # i >= 0 은 범위 벗어나는거 방지 위해
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1

    answer = 0
    # 배달이나 수거가 안된 곳이 있는지 체크하기
    while i >= 0 or j >= 0:
        answer += (max(i, j) + 1) * 2 # answer엔 i랑 j 중 큰 것을 더해 줌, *2인 이유는 갈 때 + 올 때라서 2번 이니까
        i = findMax(i, deliveries, cap) # 배달
        j = findMax(j, pickups, cap) # 수거

    return answer
