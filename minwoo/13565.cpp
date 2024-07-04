#include <iostream>
#include <vector>
using namespace std;

vector<vector<char>> grid;
vector<vector<bool>> visited;
int N, M;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

bool dfs(int x, int y) {
    if (x < 0 || y < 0 || x >= N || y >= M || visited[x][y] || grid[x][y] == '1') return false;
    visited[x][y] = true;
    if (x == N - 1) return true; // Reached bottom row
    for (int i = 0; i < 4; ++i) {
        if (dfs(x + dx[i], y + dy[i])) return true;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    grid.resize(N, vector<char>(M));
    visited.resize(N, vector<bool>(M, false));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> grid[i][j];
        }
    }

    for (int i = 0; i < M; ++i) {
        if (grid[0][i] == '0' && dfs(0, i)) {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";
}
