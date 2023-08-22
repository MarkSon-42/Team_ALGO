from collections import deque

def solution(bridgeLength, weight, truckWeights):
    answer = 0
    # 다리를 건넌 트럭들
    complete = []
    
    n = len(truckWeights)
    q = deque(truckWeights)
    
    # 다리 역할을 하는 큐
    bridge = deque()
    
    # 초단위로 계속 작업을 수행한다.
    while True:
        if len(complete) == n:
            break
        # 현재 다리를 체크한다.
        answer += 1
        # 동시에 건널 수 있는 트럭 
            
        # 대기트럭에서 leftpop 후, 다리에 진입하는 시간과 트럭을 튜플로 넣어준다.
        
        
    # 만약, 현재 트럭 + leftpop 한 값이 weight
    
    return answer