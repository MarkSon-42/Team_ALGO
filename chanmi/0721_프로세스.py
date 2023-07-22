import copy

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

        # 현재 남은 튜플 중 우선 순위 찾기
        max_prio = -100
        for prio in tuple_prio:
            if prio[1] >= max_prio:
                max_prio = prio[1]

        # 우선순위 중복의 경우
        max_count = priorities.count(max_prio)

        # 실행 순서 저장을 위한 임시 리스트
        tmp_list = []
        
        # 해당하는 우선순위가 여러개일 경우 저장용 리스트
        tmp_tuple_list = copy.deepcopy(tuple_prio)

        for prio in tmp_tuple_list:
            # 최대 priority 아닌거 뒤로 보내기
            if prio[1] < max_prio:

                tmp_data = prio
                # 앞에서 지우고 뒤로 보내기
                tuple_prio.remove(prio)
                tuple_prio.append(prio)

            # 최대인 경우    
            else:
                execute_list.append(prio[0])
                tuple_prio.remove(prio)
                max_count -= 1

                if max_count == 0:
                    break
        
    answer = execute_list.index(location)

    return answer + 1