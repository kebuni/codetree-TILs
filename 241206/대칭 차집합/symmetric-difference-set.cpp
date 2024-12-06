#include <iostream>
#include <unordered_set>
using namespace std;

unordered_set<int> A;
unordered_set<int> B;

int main() {
    int numA, numB;
    cin >> numA >> numB;
    for(int i=0; i<numA; i++){
        int input;
        cin >> input;
        A.insert(input);
    }
    for(int i=0; i<numB; i++){
        int input;
        cin >> input;
        if (A.find(input)!=A.end()){
            A.erase(input);
        }
        else
            B.insert(input);
    }
    cout << A.size() + B.size();
    return 0;
}