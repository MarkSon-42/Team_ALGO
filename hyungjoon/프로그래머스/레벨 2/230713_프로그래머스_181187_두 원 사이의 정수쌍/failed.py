import math

def solution(r1, r2):
    # 1. 크기가 서로 다르고, r1 < r2 이므로 최소 8개의 점이 있다.
    answer = 8
    temp = 0
    # 2. 굳이 다 구할 필요 없다. 1사분면에 있는 사이에 정수만 구해서 *4 해준값 + answer 해주면됨
    # r1 == 2 and r2 가 아래와 같을 때 정수 쌍의 개수
    # 5 -> 12
    # 4 -> 7
    # 3 -> 3
    # 원점이 0, 0 인 원에서 x = i 일 때 y 값은 y**2 = r**2 - x**2
    # 따라서 y = sqrt(r**2 - x**2)
    
    # 3. 위 공식에 따라서, r2의 y값과 r1의 y값을 빼준 것에 int를 씌우면 점의개수가 도출된다.
    for x in range(r2):
        # 3-1. x, y == 0일 때 원의 정수좌표는 포함하지 않는다.
        if (x == 0 and r2 - r1 == 1):
            continue
        r1Y = math.sqrt(r1**2 - x**2)
        r2Y = math.sqrt(r2**2 - x**2)
        
        dots = int(r2Y - r1Y)
        temp += dots
    
    
    return answer + temp*4
print(solution(2, 4))