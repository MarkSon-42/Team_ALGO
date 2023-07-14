# 시간 복잡도를 줄이기 위해 방법을 생각하다가 투포인터 방식이라는 아이디어를 질문하기에서 키워드만 보고 바로 코드 적용해서 누적합과 구간합, 투포인터 두가지를 적용해서 시간 복잡도를 O(N)으로 줄여서 성공
# 구간합, 누적합 개념 참고 : https://jih3508.tistory.com/50
# 구간합 = 누적합 구간 간의 차이를 뺀 것
def solution(sequence, k):
    s_idx, e_idx = -1, -1
    if k not in sequence: # k값이 sequence 배열안에 없을때
        n = len(sequence)
        prefix_sum = [0] * (n + 1) # 구간의 합을 담을 배열 생성
        for i in range(1, n + 1): # prefix_sum[i-1]과 같은 위치의 sequence 값을 넣는다.
            prefix_sum[i] = prefix_sum[i - 1] + sequence[i - 1]

        i, j = 0, 1
        while j <= n: # j가 sequence의 배열의 길이보다 작거나 같을 때까지 반복
            current_sum = prefix_sum[j] - prefix_sum[i]  # 구간합의 구간 간 차이 = 현재 부분의 합

            # 투포인터 알고리즘 사용
            if current_sum == k:  # 합이 k와 일치하는 경우
                if s_idx == -1 or e_idx - s_idx > j - i - 1: # 이전에 구간이 발견되지 않았을 때 -> 처음으로 최소 길이의 부분합을 찾았을 때, 
                    #s_idx는 -1므로 s_idx가 -1 or j, i 두 값의 차이를 비교하여 현재 구간 이전에 찾은 구간보다 더 짧은 경우에만 시작 인덱스와 끝 인덱스를 업데이트한다.
                    # 가장 짧은 길이의 부분 합의 시작 인덱스와 끝 인덱스를 구하기 위함
                    s_idx, e_idx = i, j - 1 # j는 1부터 시작했으므로 -1
                i += 1  # 시작 인덱스 증가하여 더 짧은 길이의 부분 시퀀스 탐색

            elif current_sum < k:  # 합이 k보다 작은 경우
                j += 1  # 끝 인덱스를 증가시켜서 다음 요소 포함하여 합을 증가 시킨다.

            else:  # 합이 k보다 큰 경우
                i += 1  # 시작 인덱스를 증가시켜서 합 줄임

    else:  # k가 시퀀스에 있는 경우에는 k값의 인덱스를 결과로 반환
        idx = sequence.index(k)
        s_idx, e_idx = idx, idx

    return [s_idx, e_idx]

