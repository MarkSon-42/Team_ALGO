def solution(N, stages):
    answer = []
    
    people_num = len(stages)
    count = [0 for i in range(N)]
    for stage in stages:
        if stage <= N:
            count[stage - 1] += 1
    
    failure = []
    total_man = people_num
    for man in count:
        if total_man == 0:
            failure.append(0)
        else:
            failure_num = man / total_man
            failure.append(failure_num)
            if man != 0:
                total_man -= man
    
    tmp_answer = []
    for i in range(N):
        tmp_answer.append([i+1, failure[i]])
    print(tmp_answer)
    
    for i in range(N):
        for j in range(i + 1, N):
            if tmp_answer[i][1] < tmp_answer[j][1]:
                tmp = tmp_answer[i]
                tmp_answer[i] = tmp_answer[j]
                tmp_answer[j] = tmp
            elif tmp_answer[i][1] == tmp_answer[j][1]:
                if tmp_answer[i][0] > tmp_answer[j][0]:
                    tmp = tmp_answer[i]
                    tmp_answer[i] = tmp_answer[j]
                    tmp_answer[j] = tmp
    print(tmp_answer)
    answer = []
    for i in range(N):
        answer.append(tmp_answer[i][0])
    return answer