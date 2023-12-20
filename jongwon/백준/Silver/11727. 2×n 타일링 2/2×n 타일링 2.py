import sys  # sys 모듈을 가져옵니다. 표준 입출력을 다루는 데 사용됩니다.

n = int(sys.stdin.readline())  # 사용자로부터 입력을 받아 정수형으로 변환하여 변수 n에 저장합니다.

dp_table = [0] * 1001  # 크기가 1001인 리스트를 생성하고 0으로 초기화합니다. 각 인덱스는 방법의 수를 저장합니다.

dp_table[0] = 1  # 초기값: 2x0 직사각형을 채우는 방법의 수는 1가지입니다.
dp_table[1] = 1  # 초기값: 2x1 직사각형을 채우는 방법의 수는 1가지입니다.

# 동적 프로그래밍을 통해 각 크기의 직사각형을 채우는 방법의 수를 구합니다.
for i in range(2, n + 1):
    dp_table[i] = dp_table[i - 1] + 2 * dp_table[i - 2]
    # 점화식을 이용하여 현재 크기의 직사각형을 채우는 방법의 수를 계산합니다.
    # 현재 위치의 값은 바로 이전 위치의 값과 그 이전의 두 칸을 더한 값으로 계산됩니다.

print(dp_table[n] % 10007)  # 2×n 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력합니다.