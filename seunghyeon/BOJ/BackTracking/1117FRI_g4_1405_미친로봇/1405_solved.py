import sys
my_input = sys.stdin.readline


def dfs(r, c, visited, total, answer):
    if len(visited) == N+1:
        answer += total

        return
    for idx in range(4):
        now_r = r + d[idx][0]
        now_c = c + d[idx][1]
        if (now_r, now_c) not in visited:
            visited.append((now_r, now_c))
            dfs(now_r, now_c, visited, total*probability[idx])
            visited.pop()


N, e_prob, w_prob, s_prob, n_prob = map(int, my_input().split())
probability = [e_prob, w_prob, s_prob, n_prob]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 동 서 남 북
answer = 0

dfs(0, 0, [(0, 0)], 1, 0)
print(answer * (0.01 ** N))
