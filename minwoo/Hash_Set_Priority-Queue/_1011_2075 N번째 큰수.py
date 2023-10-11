# N*N을 다 돌면서 대소비교를 하는것은 절대 아닐것
# 우선순위 큐 기본문제
# 문제에서 N번째로 큰 수를 찾는것이고 주어지는 배열이 N*N이기 때문에 queue size를 N이하로 제한하면 된다


import heapq

pq = []
n = int(input())

for _ in range(n):
    num_arr = map(int, input().split())
    for num in num_arr:
        if len(pq) < n:
            heapq.heappush(pq, num)
        else:
            if pq[0] < num:
                heapq.heappop(pq)  # 더 큰수가 있다면 갱신해주기
                heapq.heappush(pq, num)

print(pq[0])