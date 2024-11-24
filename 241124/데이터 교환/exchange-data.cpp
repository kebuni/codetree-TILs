#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 5;
    int b = 6;
    int c = 7;
    int temp;

    temp = c;
    c = b;
    b = a;
    a = temp;

    cout << a << endl << b << endl << c;

    return 0;
}