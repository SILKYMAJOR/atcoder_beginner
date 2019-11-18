#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }
 
  // (ここで"試合結果の表"の2次元配列を宣言)
  vector<vector<char>> result(N, vector<char>(N, '-'));
 
  // o x をつけていく
  for (int i = 0; i < M; i++) {
    result.at(A.at(i) - 1).at(B.at(i) - 1) = 'o';
    result.at(B.at(i) - 1).at(A.at(i) - 1) = 'x';
  }
 
  for (vector<char> row : result){
    int count=0;
    for (char str : row){
      count++;
      if(count==N){
        cout << str;
      }else{
        cout << str << ' ';
      }
    }
    cout << endl;
  }
}
