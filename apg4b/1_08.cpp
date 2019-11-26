#include <bits/stdc++.h>
using namespace std;

int main() {
  int p;
  cin >> p;

  // パターン1
  if (p == 1) {
    int price, num;
    cin >> price >> num;
    cout << price * num << endl;
  }

  // パターン2
  if (p == 2) {
    string text;
    int price, num;
    cin >> text >> price >> num;
    cout << text << "!" << endl;
    cout << price * num << endl;
  }

}

