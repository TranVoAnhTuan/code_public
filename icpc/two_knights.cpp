#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll k;
int main(){
  IOS;
  freopen("test.inp", "r", stdin);
  freopen("test.out", "w", stdout);
  cin >> k;
  fi(n, 1, k){
    ll totalPosition = (n*n) * (n*n-1)/2;
    ll attackPosition = 4 * (n - 1) * (n - 2);
    cout << totalPosition - attackPosition << '\n';
  }
  return 0;
}
