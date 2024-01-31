import heapq

def solution(n, k, enemy):
    answer = 0

    mjk = []

    for e in enemy:
        n -= e
        if n >= 0:
            heapq.heappush(mjk, -e)
        else:
            if k > 0:
                k -= 1
                heapq.heappush(mjk, -e)
                n -= heapq.heappop(mjk)
            else:
                break

        answer += 1


    return answer
