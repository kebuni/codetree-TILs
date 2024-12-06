#include <iostream>
#include <map>
#include <string>
using namespace std;

map<string,int> m;

int main() {
    int N;
    cin >> N;
    for (int i=0; i<N;i++){
        string input;
        cin >> input;
        m[input]++;
    }

    for(auto it:m){
        cout << it.first << " " << it.second << endl;
    }

    return 0;
}