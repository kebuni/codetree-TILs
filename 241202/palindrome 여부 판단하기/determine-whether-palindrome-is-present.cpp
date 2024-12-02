#include <iostream>
#include <string>
using namespace std;

string reverse(string &a){
    string reversed = "";
    for(int i=a.length()-1; i>=0; i--){
        reversed += a[i];
    }
    return reversed;
}

int main() {

    string s;
    string reversed;

    cin >> s;
    reversed = reverse(s);

    if (s == reversed)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}