#include <bits/stdc++.h>
#include <cstdio>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll n;
int main(){
  IOS;

  // freopen("test.inp", "r", stdin);
  // freopen("test.out", "w", stdout);
  cin >> n;
  while(n--){
    ll y, x, ans;
    cin >> y >> x;
    ll tmp = max(y, x);
    if(tmp % 2){
      if(y == tmp){
        ans =(tmp - 1) * (tmp - 1) + x;
      } else{
        ans = tmp * tmp + 1 - y;
      }
    }
    else{
        if(x == tmp){
          ans = (tmp - 1) * (tmp - 1) + y;
        } else{
          ans = tmp * tmp - x + 1;
        }
    }
    cout << ans << '\n';
  }
  return 0;
}
