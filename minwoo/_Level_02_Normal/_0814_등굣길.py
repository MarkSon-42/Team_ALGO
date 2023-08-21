# 문제에서 웅덩이 좌표를 2,2로 줘놓고
# 행렬에 대한 기준 ( 어디가 행이고 어디가 열인지? )이 명확하지 않음

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # *--dp배열 초기화. 왜 +1로 패딩을 넣어주는지? -> 인덱싱 오류방지 및 편의성을 위해.
    dp[1][1] = 1  # 시작위치 집은 1로 마킹

    # 웅덩이는 -1로 마킹.
    for i, j in puddles:
        dp[j][i] = -1


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 웅덩이 만나면 경로 개수 초기화 하고 넘어가주기
                dp[i][j] = 0
                continue

            dp[i][j] += (dp[i - 1][j] + dp[i][j-1]) % 1_000_000_007

    return dp[n][m]

# 메모이제이션을 적용한 풀이들도 있는거 같은데 우선 기본 dp부터 익숙해지면 적용해보자..


solution(4, 3, [[2, 2]])


#    *dp배열 초기화시 +1로 패딩해주는 이유*
# DP 배열을 초기화할 때 입력 배열의 크기에 추가 "+1"을 추가하는 것은 동적 프로그래밍 문제에서 사용되는 일반적인 기술입니다.
# 이 접근 방식은 1 기반 인덱싱(인간에게 더 직관적임)을 0 기반 인덱싱(프로그래밍에 더 편리함)으로 변환하는 아이디어에 뿌리를 두고 있습니다.
#
# 많은 동적 프로그래밍 문제에서 입력 또는 문제 문은 인덱싱이 0이 아닌 1부터 시작하는 1 기반 인덱싱을 사용할 수 있습니다.
# 그러나 Python을 포함한 대부분의 프로그래밍 언어는 인덱싱이 0부터 시작하는 0 기반 인덱싱을 사용합니다.
# 입력/인덱싱 스타일과 프로그래밍 언어 스타일 사이의 이러한 격차를 해소하기 위해 배열 차원에 "+1"을 추가하는 것이 표준 관행입니다.
#
# 이것을 문제와 연관시키고 왜 관련이 있는지 살펴보겠습니다.
#
# 문제에서 그리드는 "m" 열과 "n" 행을 사용하여 설명됩니다. 입력이 1 기반 인덱싱에서 그리드를 설명하는 경우
# 열은 1에서 "m"까지 인덱싱되고 행은 1에서 "n"까지 인덱싱됩니다.
# 그러나 대부분의 프로그래밍 언어에서 배열을 생성할 때 0 기반 인덱싱을 사용하는 것이 더 자연스럽습니다.
# 인덱스 범위는 열에 대해 0에서 "m-1"까지, 행에 대해 0에서 "n-1"까지입니다.
#
# DP 배열의 두 차원에 "+1"을 추가하면 기본적으로 0부터 시작하든 1부터 시작하든 모든 유효한 인덱스에 대한 값을 보유할 수 있는 배열을 만드는 것입니다.
# 이렇게 하면 오프 바이 원 오류를 방지하고 인덱싱 차이를 지속적으로 조정하지 않고도 입력 그리드의 인덱스와 DP 배열의 인덱스 간에 쉽게 매핑할 수 있습니다.