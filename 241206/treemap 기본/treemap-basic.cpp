#include <iostream>
#include <map>
#include <string>
using namespace std;

map<int, int> m;

int main() {
    int N;
    cin >> N;
    for (int i=0; i<N; i++){
        string command;
        cin >> command;
        if (command=="add"){
            int k, v;
            cin >> k >> v;
            m[k] = v;
        }
        else if (command == "remove"){
            int k;
            cin >> k;
            m.erase(k);
        }
        else if (command == "find"){
            int k;
            cin >> k;
            if(m.find(k)==m.end()){
                cout << "None" << endl;
            }
            else{
                cout << m[k] << endl;
            }
        }
        else{
            if (m.empty())
                cout << "None" << endl;
            else{
                for(auto it:m){
                    cout << it.second << " ";
                }
                cout << endl;
            }
            
        }
    }
    return 0;
}