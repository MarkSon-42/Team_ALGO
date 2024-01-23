from collections import deque

def solution(order):
    # 1. 주어진 순서대로 상자로 메인 벨트를 초기화합니다.
    main_belt = deque([i for i in range(1, len(order) + 1)])
    # 2. 보조 벨트를 빈 스택으로 초기화합니다.
    sub_belt = []
    # 3. 트럭에 실은 상자의 수를 추적하기 위해 카운터를 초기화합니다.
    counter = 0
    idx = 0

    # 4. 메인 벨트가 비어 있지 않은 동안, 메인 벨트의 앞에 있는 상자를 확인합니다.
    while main_belt:
        # 5. 상자가 트럭에 실을 다음 상자라면, 메인 벨트에서 제거하고 카운터를 증가시킵니다.
        if order[idx] == main_belt[0]:
            main_belt.popleft()
            counter += 1
            idx += 1
        else:
            # 6. 상자가 트럭에 실을 다음 상자가 아니라면, 메인 벨트에서 제거하고 보조 벨트에 푸시합니다.
            sub_belt.append(main_belt.popleft())

        # 7. 메인 벨트를 확인한 후, 보조 벨트를 확인합니다. 보조 벨트의 맨 위에 있는 상자가 트럭에 실을 다음 상자라면, 보조 벨트에서 팝하고 카운터를 증가시킵니다.
        while sub_belt and order[idx] == sub_belt[-1]:
            sub_belt.pop()
            counter += 1
            idx += 1

    # 9. 카운터를 반환합니다.
    return counter


# tc O(n)
