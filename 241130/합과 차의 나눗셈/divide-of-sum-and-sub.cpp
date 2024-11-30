#include <iostream>
using namespace std;

int main() {
    cout << fixed;
    cout.precision(2);

    int a,b;
    cin >> a >> b;
    cout << (double)(a+b) / (a-b);
    return 0;
}