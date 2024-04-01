#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll t;
int main(){
  IOS;
  cin >> t;
  ll a, b;
  while(t--){
    cin >> a >> b;
    if((a+b)%3 || a > 2 * b || b > 2 * a){
      cout << "NO" << '\n';
    } else{
      cout << "YES" << '\n';
    }
  }
  return 0;
}
