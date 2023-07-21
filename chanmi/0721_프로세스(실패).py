def solution(priorities, location):
        
    # 실행 순서를 저장하는 리스트
    execute_list = []
    # 처리 용이성을 위해 인덱스와 함께 튜플로 묶어서 저장
    tuple_prio = []
    for i in range(len(priorities)):
        tuple_prio.append((i, priorities[i]))

    while True:
        if len(tuple_prio) == 0:
            break

        # print("현재 데이터 :", tuple_prio)
        # 현재 남은 튜플 중 우선 순위 찾기
        max_prio = -100
        for prio in tuple_prio:
            if prio[1] >= max_prio:
                max_prio = prio[1]

        # 실행 순서 저장을 위한 임시 리스트
        tmp_list = []
        
        # 해당하는 우선순위가 여러개일 경우 저장용 리스트
        delete_list = []
        for prio in tuple_prio:
            if prio[1] >= max_prio:
                tmp_list.append(prio[0])
                delete_list.append(prio)
        tmp_list.sort(key = lambda x:x, reverse=True)
        execute_list += tmp_list
        
        # print("실행 프로세스 :", execute_list)

        # print("지울 프로세스 :", delete_list)
        for item in delete_list:
            tuple_prio.remove(item)
    
    answer = execute_list.index(location)
    return answer + 1

solution([2, 1, 3, 2], 2)