#include <iostream>
#define MAX 100
using namespace std;

int n, m;
int grid[MAX][MAX];
bool visited[MAX][MAX] = {false,};

bool inRange(int x,int y){
    return (0<=x && x<n && 0<=y && y<m);
}

bool canGo(int x,int y){
    if (!inRange(x,y))
        return false;
    if (visited[x][y])
        return false;
    if (grid[x][y]==0)
        return false;
    return true;
}

void dfs(int x, int y){
    int dx[2] = {1,0};
    int dy[2] = {0,1};
    for (int d=0;d<2;d++){
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (canGo(nx,ny)){
            visited[nx][ny] = true;
            dfs(nx,ny);
        }
    }
    return;
}

int main() {

    cin >> n >> m;
    for(int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            cin >> grid[i][j];
        }
    }

    visited[0][0] = true;
    dfs(0,0);
    if (visited[n-1][m-1])
        cout << 1;
    else
        cout << 0;

    return 0;
}