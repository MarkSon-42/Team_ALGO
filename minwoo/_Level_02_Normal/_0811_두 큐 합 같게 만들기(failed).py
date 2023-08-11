def solution(queue1, queue2):
    answer = 0
    queue_sum = sum(queue1) + sum(queue2)
    if queue_sum % 2 != 0:  # 두 큐의 합을 같게 만들 수 없는 경우
        return -1
    elif sum(queue1) == sum(queue2):
        return 0  # 두 큐의 합이 이미 같은 경우
    else:
        goal_queue = sum(queue1) + sum(queue2) // 2
        while sum(queue1) == goal_queue or sum(queue2) == goal_queue:
            if sum(queue1) > sum(queue2):
                pass

        #  큰 큐에서 작은 큐로 옮기는 것을 반복하면 큐가 같아질텐데
        #  여기에 로직을 뭘 짜야할 지 모르겠음..
        #  sum()이 while안에서 돌면 무조건 시간초과남 ( 문제에 힌트.. )


    return answer