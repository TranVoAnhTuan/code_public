
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll n, s = 0, a[maxV];
int main(){
  IOS;
  // freopen("test.inp", "r", stdin);
  // freopen("test.out", "w", stdout);
  cin >> n;
  fi(i,1,n){
    cin >> a[i]; 
    s += a[i];
  }
  cout << (n * (n + 1))/2 - s; 
  return 0;
}
