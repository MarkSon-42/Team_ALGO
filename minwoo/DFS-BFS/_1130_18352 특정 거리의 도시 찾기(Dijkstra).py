print('Dijkstra Algorithm')

# # 코드 c++
# # 신기해서 가져와봄
#
# # include <vector>
# # include <queue>
#
# // 아직
# 방문하지
# 않은
# 노드
# 중
# // 가장
# 거리값이
# 작은
# 노드의
# 인덱스
# 반환
# int
# FindSmallestNode()
# {
#     int
# min_dist = INF;
# int
# min_idx = -1;
# for (int i = 0; i <= N; i++)
# {
# if (visited[i] == true)
# continue;
# if (dist[i] < min_dist)
#     {
#         min_dist = dist[i];
#     min_idx = i;
#     }
#     }
#     return min_idx;
#     }
#
#     // 다익스트라
#     void
#     Dijkstra()
#     {
#     for (int i = 1; i <= N; i++)
#         dist[i] = map[start][i]; // 시작
#         노드와
#         인접한
#         정점에
#         대해
#         거리
#         계산
#
#     dist[start] = 0;
#     visited[start] = true;
#
#     for (int i = 0; i < N - 1; i++)
#         {
#             int
#         new_node = FindSmallestNode();
#         visited[new_node] = true;
#
#         for (int j = 0; j <= N; j++)
#         {
#         if (visited[j] == true)
#         continue;
#     if (dist[j] > dist[new_node] + map[new_node][j])
#         dist[j] = dist[new_node] + map[new_node][j];
#     }
#     }
#     }