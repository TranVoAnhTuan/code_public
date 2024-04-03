#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
ll n;
int main(){
  IOS;
  int n;
  cin >> n;
  string grayCode = "";
  fi(i, 0, (1 << n) - 1){
    int ans = i ^ (i >> 1);
    fd(j, n - 1, 0){
      grayCode += ((ans >> j) & 1) ? '1' : '0';
    }
    grayCode += '\n';
  }
  cout << grayCode;
  return 0;
}

