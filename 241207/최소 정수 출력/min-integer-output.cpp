#include <iostream>
#include <queue>
using namespace std;

priority_queue<int,vector<int>,greater<int> > pq;

int main() {
    int N;
    cin >> N;
    for (int i=0; i<N ; i++){
        long long input;
        cin >> input;
        if (input == 0){
            if(pq.empty())
                cout << 0 << endl;
            else{
                cout << pq.top() << endl;
                pq.pop();
            }
            
        }
        else{
            pq.push(input);
        }
    }
    return 0;
}