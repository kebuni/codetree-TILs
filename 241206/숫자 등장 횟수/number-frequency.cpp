#include <iostream>
#include <unordered_map>
using namespace std;

unordered_map<int,int> m;

int main() {
    int N, M;
    cin >> N >> M;
    for (int i=0; i<N;i++){
        int input;
        cin >> input;
        m[input]++;
    }
    for (int i=0; i<M;i++){
        int input;
        cin >> input;
        cout << m[input] << " ";
    }
    return 0;
}