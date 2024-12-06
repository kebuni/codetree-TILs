#include <iostream>
#include <set>
using namespace std;

set<int> s;

int main() {
    int N, M;
    cin >> N >> M;
    for(int i =0; i<N ; i++){
        int input;
        cin >> input;
        s.insert(input);
    }
    for(int i =0; i<M ; i++){
        int num;
        cin >> num;
        set<int>::iterator it;
        it = s.upper_bound(num);
        it--;
        if(it == s.end())
            cout << -1 << endl;
        else{
            cout << *it << endl;
            s.erase(*it);
        }

    }
    return 0;
}