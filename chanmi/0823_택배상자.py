def solution(order):
    # 컨테이너 벨트 = 큐
    # 보조 컨테이너 벨트 = 스택
    
    # 1 2 3 4 5 상자
    # 3 4 2 1 5 순서
    
    # order을 넣는 순서대로 맞춰주는 작업
    box = [0] * len(order)
    index = 1
    for item in order:
      box[item - 1] = index
      index += 1

    truck = []
    sub = []
    count = 1
    for item in box:
        # 넣는 순서가 아니면 보조 컨베이어 벨트에 넣음
        if item != count:
            sub.append(item)

        # 넣는 순서가 맞으면 트럭에 실음
        else:
            truck.append(item)
            count += 1

            # 트럭에 실은 이후 보조 컨베이어 벨트에서 트럭에 실을 게 있는지 확인
            # 없으면 이후 돌아갈 for문을 통해 다시 컨베이어 벨트 확인
            while True:
                if len(sub) != 0 and sub[-1] == count:
                    truck.append(sub.pop())
                    count += 1
                # 보조 컨베이어 벨트의 길이가 0이거나 가장 바깥에 있는게 순서가 아닐 경우 더 볼 필요 없음
                else:
                    break
    return len(truck)