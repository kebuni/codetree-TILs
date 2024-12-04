#include <iostream>
#define MAX 1000
using namespace std;

bool graph[MAX + 1][MAX + 1] = { false, };
bool visited[MAX + 1] = { false, };

void dfs(int v, int n) {

	// v로부터 갈 수 있는 곳들에 대해 dfs
	for (int i = 1; i <= n;i++) {
		if (graph[v][i] && !visited[i]) {
			visited[i] = true;
			dfs(i, n);
		}
	}

	return;
}

int main() {
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < m;i++) {
		int u, v;
		cin >> u >> v;
		graph[u][v] = graph[v][u] = true;
	}

	visited[1] = true;
	dfs(1,n);

	int ans = 0;
	for (int i = 2; i <= n; i++) {
		if (visited[i])
			ans++;
	}
	cout << ans;

	return 0;
}