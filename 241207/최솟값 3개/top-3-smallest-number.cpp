#include <iostream>
#include <queue>

#define MAX_N 100000

using namespace std;

// 변수 선언
int n;
int arr[MAX_N];
priority_queue<int> pq;  

int main() {
    // 입력:
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    // priority queue를 이용하여 진행합니다.
    for(int i = 0; i < n; i++) {
        // 해당 숫자를 priority queue에 넣어줍니다.
        // 이때 최솟값을 구하기 위해서는
        // -를 붙여서 넣어줘야 함에 유의합니다.
        pq.push(-arr[i]);
        
        if(pq.size() >= 3) {
            // 주어진 수가 3개 이상이라면 가장 작은 숫자 3개의 곱을 출력합니다.
            int x = -pq.top(); pq.pop();
            int y = -pq.top(); pq.pop();
            int z = -pq.top(); pq.pop();

            cout << (long long)x * y * z << endl;

            pq.push(-x);
            pq.push(-y);
            pq.push(-z);
        }
        else {
            // 아직 주어진 숫자의 수가 3개가 되지 않으면 -1을 출력합니다.
            cout << -1 << endl;
        }
    }
    return 0;
}