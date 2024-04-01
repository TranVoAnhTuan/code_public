#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll n, k;
vector<ll> a;
int main(){
  IOS;
  freopen("test.inp", "r", stdin);
  freopen("test.out", "w", stdout);
  cin >> n >> k;
  ll maxValue = 0;
  while(n--){
    ll x;
    cin >> x;
    a.push_back(x);
    maxValue = max(x, maxValue);
  }
  ll ans = 0, res;
  fd(x, maxValue, 1){
    fi(i, 0, a.size() - 1){
      if(a[i] % x == 0){
        ans++;
      }
    }
    if(ans >= k){
      cout << x;
      break;
    }else{
      ans = 0;
    }
  }
  return 0;
}
