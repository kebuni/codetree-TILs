#include <iostream>
#include <unordered_map>
using namespace std;

unordered_map<int,int> m;

int main() {
    
    int N;
    cin >> N;

    for (int i=0; i<N;i++){
        long long x, y;
        cin >> x >> y;
        if(m.find(x)==m.end())
            m[x] = y;
        else
            m[x] = m[x] > y ? y : m[x];
        //cout << m[x] << endl;
    }

    long long ans=0;
    for (auto it:m)
        ans += it.second;
    cout << ans;

    return 0;
}