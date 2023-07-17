def solution(plans):

    plans.sort(key = lambda x:x[1])
    # 해야하는 일을 저장하는 큐
    ready_queue = []
    
    # 현재 시간을 저장하는 리스트. [hour, minute] 형식.
    current_time = [0, 0]
    
    finish_list = []
    
    for plan in plans:
        # print("데이터 소개:", plan)
        # 대기 큐에 아무 것도 없을 경우(실행 중인 프로그램도 없음)
        if len(ready_queue) == 0:
            ready_queue.append(plan)
            
            # print(ready_queue[-1][0], "집어 넣음(최초)")

            # 현재 시각 지정하기
            time_check = plan[1].split(':')
            current_time = [int(time_check[0]), int(time_check[1])]
            
        
        # 대기 큐에 뭔가 있을 경우(뭔가 이전에 실행중)
        else:
            # 대기 큐에 있는 실행 시간 가져오기
            running_time = int(ready_queue[-1][2])
            
            # 이전 현재 시각과 실행 시간을 더했을 때, 지금 가져온 과제의 시작 시간과 비교하기
            tmp_time = time_add(current_time, running_time)
            # print("예상 과제 종료 시간", tmp_time)
            
            time_check = plan[1].split(':')
            future_time = [int(time_check[0]), int(time_check[1])]
            # print("데이터 과제 시작 시간", future_time)
            
            # 만약 이전 현재 시각과 실행 시간을 더했는데 과제의 시작 시간보다 앞서면, 이미 끝난 업무임
            # 이 경우 레디 큐에 남은 시간이 있는지 확인 필요
            if time_compare(tmp_time, future_time) == 0:
                # print(ready_queue[-1][0], "이르게 완료")
                finish_list.append(ready_queue[-1][0])
                ready_queue.pop()
                
                # 레디 큐 확인 필요
                while True:
                    # print("레디큐 확인 :", ready_queue)
                    if len(ready_queue) == 0:
                        # print("레디큐 대기 없음.", plan[0], "집어 넣음")
                        current_time = future_time
                        break
                    else:
                        # 대기 큐에 있는 실행 시간 가져오기
                        running_time = int(ready_queue[-1][2])
                        
                        # 추가로 실행 가능 남은 시간
                        remain_time = time_minus(future_time, tmp_time)
                        
                        # 다 실행 못하는 경우
                        if remain_time < running_time:
                            # print(ready_queue[-1][0], "전부 실행 못함.", running_time-remain_time, "분 더 필요함.")
                            ready_queue[-1][2] = running_time - remain_time
                            current_time = future_time
                            break
                        
                        # 딱 맞게 실행
                        elif remain_time == running_time:
                            # print(ready_queue[-1][0], "전부 실행함. 시간 딱 맞음.")
                            finish_list.append(ready_queue[-1][0])
                            ready_queue.pop()
                            
                            current_time = future_time
                            break
                            
                        # 실행하고 시간이 또 남는 경우
                        else:
                            remain_time -= running_time
                            # print(ready_queue[-1][0], "전부 실행함. 실행 후 시간 남음.")
                            finish_list.append(ready_queue[-1][0])
                            ready_queue.pop()
                            tmp_time = time_add(tmp_time, running_time)
                            current_time = tmp_time
                            
            # 만약 딱 맞게 끝날 경우
            elif time_compare(tmp_time, future_time) == -1:
                # print(ready_queue[-1][0], "전부 실행함. 시간 딱 맞음.")
                finish_list.append(ready_queue[-1][0])
                ready_queue.pop()
                
            
            # 할 일 다 못끝내는 경우
            else:
                time1 = time_minus(tmp_time, future_time)
                # print(ready_queue[-1][0], "다 못끝냄")
                ready_queue[-1][2] = time1
                
            ready_queue.append(plan)
            time_check = plan[1].split(':')
            current_time = [int(time_check[0]), int(time_check[1])]

        # 마지막 아이템인 경우 이후 레디큐 처리 필요        
        if plan == plans[-1]:
            while True:
                # print("레디큐 확인 :", ready_queue)
                if len(ready_queue) == 0:
                    # print("큐 종료")
                    break
                else:
                    finish_list.append(ready_queue[-1][0])
                    # print(ready_queue[-1][0], "마무리")
                    ready_queue.pop()

    return finish_list

# 시간 더해주는 함수(귀찮아서 만들음)
def time_add(hour, minute):
    hour[1] += minute
    while True:
      if hour[1] >= 60:
          hour[0] += 1
          hour[1] -= 60
      else:
        break
    return hour

# 시간 차이 구해주는 함수(귀찮아서 만들음)
def time_minus(hour1, hour2):
    minute1 = hour1[0] * 60 + hour1[1]
    minute2 = hour2[0] * 60 + hour2[1]
    if minute1 - minute2 > 0:
        return minute1 - minute2
    else:
        return minute2 - minute1 


# 시간 비교해주는 함수(귀찮아서+코드 깔끔하게 쓰려고 만들음)
# 앞쪽 시간이 크면 1, 아니면 0, 동일하면 -1 반환
def time_compare(hour1, hour2):
    # print("\nhour1 :", hour1)
    # print("hour2 :", hour2, '\n')
    # hour1이 hour2보다 나중의 시간인 경우
    if hour1[0] > hour2[0]:
        return 1
    elif hour1[0] == hour2[0] and hour1[1] > hour2[1]:
        return 1
    
    # hour1과 hour2가 같은 시간일 경우    
    elif hour1[0] == hour2[0] and hour1[1] == hour2[1]:
        return -1
    
    # hour2가 hour1보다 나중의 시간일 경우
    else:
        return 0