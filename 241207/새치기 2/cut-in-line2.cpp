#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define MAX_N 100000
#define MAX_M 10

// 사람들을 나타내는 노드입니다.
struct Node {
    // 사람의 번호를 나타냅니다.
    string name;
    Node *prev, *next;

    Node(string name) : name(name), prev(nullptr), next(nullptr) {}
};

// 사람들을 나타내는 노드들을 저장합니다.
Node *nodes[MAX_N + 1];

// 각 줄의 시작과 끝을 나타냅니다.
Node *head[MAX_M + 1], *tail[MAX_M + 1];

// 각 사람이 몇 번 줄에 서있는지 나타냅니다.
int lineNum[MAX_N + 1];

// 각 사람의 이름들을 번호로 바꿔줍니다.
unordered_map<string, int> personId;

// 두 사람을 연결합니다.
void connect(Node *s, Node *e) {
    if (nullptr != s) s->next = e;
    if (nullptr != e) e->prev = s;
}

// i번 사람을 집에 보냅니다.
void del(Node *i) {
    // i번 사람이 어느 줄에 서있는지 확인합니다.
    int l = lineNum[personId[i->name]];

    // i번 사람이 어느 줄에도 서있지 않다면 아무것도 하지 않습니다.
    if (l == 0) return;

    // i번 사람이 줄의 시작이었다면 줄의 시작을 다음 사람으로 바꿉니다.
    if (head[l] == i) head[l] = head[l]->next;
    // i번 사람이 줄의 끝이었다면 줄의 끝을 이전 사람으로 바꿉니다.
    if (tail[l] == i) tail[l] = tail[l]->prev;

    // i번 사람을 줄에서 뺍니다.
    // 원래 i번 사람의 이전 사람과 다음 사람을 연결합니다.
    if (nullptr != i->prev) i->prev->next = i->next;
    if (nullptr != i->next) i->next->prev = i->prev;

    // i번 사람이 어느 줄에도 서있지 않다고 표시합니다.
    lineNum[personId[i->name]] = 0;
    i->next = i->prev = nullptr;
}

// a번 사람을 b번 사람 앞에 서게 합니다.
void insertFront(Node *a, Node *b) {
    // b번 사람이 어느 줄에 서있는지 확인합니다.
    int lineNumB = lineNum[personId[b->name]];
    // b번 사람이 해당 줄의 맨 앞이었다면, a번 사람을 줄의 맨 앞으로 만듭니다.
    if (head[lineNumB] == b) head[lineNumB] = a;
    // a번 사람을 해당 줄에서 뺍니다.
    del(a);

    // a번 사람을 b번 사람 앞에 서게 합니다.
    connect(b->prev, a);
    connect(a, b);

    // a번 사람이 어느 줄에 서있는지 표시합니다.
    lineNum[personId[a->name]] = lineNumB;
}

// a번 사람부터 b번 사람까지를 c번 사람 앞에 이동합니다.
void move_partial_front(Node *a, Node *b, Node *c) {
    // a, c번 사람이 어느 줄에 서있는지 확인합니다.
    int lineNumA = lineNum[personId[a->name]];
    int lineNumC = lineNum[personId[c->name]];

    // a번 사람이 해당 줄의 맨 앞이었다면, 해당 줄의 맨 앞 사람을 b번 사람의 뒤로 변경합니다.
    if (head[lineNumA] == a) head[lineNumA] = b->next;
    // b번 사람이 해당 줄의 맨 끝이었다면, 해당 줄의 맨 끝 사람을 a번 사람의 앞으로 변경합니다.
    if (tail[lineNumA] == b) tail[lineNumA] = a->prev;

    // a번 사람부터 b번 사람까지를 줄에서 뺍니다.
    // 이때 a번 사람의 이전 사람과 b번 사람의 다음 사람을 연결합니다.
    connect(a->prev, b->next);

    // c번 사람 앞에 a번 사람부터 b번 사람까지를 넣습니다.
    // 이때 c번 사람이 해당 줄의 맨 앞이었다면, a번 사람을 줄의 맨 앞으로 만듭니다.
    if (head[lineNumC] == c) {
        connect(b, c);
        head[lineNumC] = a;
    }
        // 아니라면, c번 사람의 이전 사람과 a번 사람을 연결합니다.
        // 또한 b번 사람과 c번 사람을 연결합니다.
    else {
        connect(c->prev, a);
        connect(b, c);
    }

    // a번 사람부터 b번 사람까지 어느 줄에 서 있는지 표시합니다.
    Node *cur = a;
    while (cur != b) {
        lineNum[personId[cur->name]] = lineNumC;
        cur = cur->next;
    }
    lineNum[personId[cur->name]] = lineNumC;
}

// 해당 줄을 전부 출력합니다.
void printLine(int l) {
    Node *cur = head[l];

    if (cur == nullptr) {
        cout << -1 << "\n";
        return;
    }

    while (nullptr != cur) {
        cout << cur->name << " ";
        cur = cur->next;
    }
    cout << "\n";
}

int main() {
    // 입력
    int n, m, q;
    cin >> n >> m >> q;

    // m 개의 줄을 입력 받습니다.
    int personNum = 1;
    for (int i = 1; i <= m; i++) {
        for (int j = 0; j < n / m; j++) {
            string t;
            cin >> t;
            personId[t] = personNum;
            lineNum[personNum] = i;

            if (j == 0) {
                tail[i] = head[i] = nodes[personNum] = new Node(t);
            } else {
                nodes[personNum] = new Node(t);
                connect(tail[i], nodes[personNum]);
                tail[i] = nodes[personNum];
            }

            personNum++;
        }
    }

    // q 개의 문자대로 시뮬레이션을 진행합니다.
    while (q--) {
        int option;
        cin >> option;

        if (option == 1) {
            string x, y;
            cin >> x >> y;
            int a = personId[x], b = personId[y];
            insertFront(nodes[a], nodes[b]);
        } else if (option == 2) {
            string x;
            cin >> x;
            int a = personId[x];
            del(nodes[a]);
        } else if (option == 3) {
            string x, y, z;
            cin >> x >> y >> z;
            int a = personId[x], b = personId[y], c = personId[z];
            move_partial_front(nodes[a], nodes[b], nodes[c]);
        }
    }

    // 출력
    for (int i = 1; i <= m; i++) printLine(i);
}