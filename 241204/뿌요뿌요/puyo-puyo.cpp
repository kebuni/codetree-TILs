#include <iostream>
#define MAX 100
using namespace std;

int n;
int cnt = 0;
int max_size = 0;
int cur_size = 1;
int grid[MAX][MAX];
int visited[MAX][MAX] = {false,};

bool inRange(int x, int y){
    return 0<=x && x<n && 0<=y && y<n;
}

bool canGo(int x, int y, int num){
    return inRange(x,y) && !visited[x][y] && grid[x][y] == num;
}

void dfs(int x, int y){
    int dx[4] = {-1,0,1,0};
    int dy[4] = {0,1,0,-1};

    for (int d=0; d<4; d++){
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (canGo(nx,ny,grid[x][y])){
            visited[nx][ny] = true;
            cur_size++;
            dfs(nx,ny);
        }
    }
    return;
}

int main() {
    
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n;j++) {
            cin >> grid[i][j];
        }
    }

    for (int i=0; i<n; i++){
        for (int j=0; j<n;j++){
            if (!visited[i][j]){
                cur_size = 1;
                visited[i][j] = true;
                dfs(i,j);
                if (cur_size >= 4)
                    cnt++;
                if (cur_size > max_size)
                    max_size = cur_size;
            }
        }
    }

    cout << cnt << " " << max_size;

    return 0;
}