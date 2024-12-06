#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

unordered_map<int,int> m;

int main() {
    int N;
    cin >> N;
    for (int i=0;i<N;i++){
        string command;
        cin >> command;
        if(command == "add"){
            int k, v;
            cin >> k >> v;
            m[k] = v;
        }
        else if (command == "find"){
            int k;
            cin >> k;
            if(m.find(k)!=m.end())
                cout << m[k] << endl;
            else
                cout << "None" << endl;
        }
        else{
            int k;
            cin >> k;
            m.erase(k);
        }
    }
    return 0;
}