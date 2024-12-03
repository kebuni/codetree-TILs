#include <iostream>
#include <vector>
using namespace std;

vector<int> v;

void print(){
    cout << "[v] "; 
    for(int i=0;i<v.size();i++){
        cout << v[i] << " ";
    }
    cout << endl;
    return;
}

int main() {

    int n;
    cin >> n;

    string command;
    int param;

    for (int i=0;i<n;i++){
        cin >> command;
        if (command == "push_back"){
            cin >> param;
            v.push_back(param);
        }
        else if (command == "pop_back"){
            v.pop_back();
        }
        else if (command == "get"){
            cin >> param;
            cout << v[param-1] << endl;
        }
        else {
            cout << v.size() << endl;
        }
        //print();
    }
    return 0;
}