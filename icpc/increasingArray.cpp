#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll n, a[maxV];
int main(){
  IOS;
  cin>>n;
  cin>>a[1];
  ll currMin = a[1];
  ll ans = 0;
  fi(i,2,n){
    cin>>a[i];
    if(a[i] >= currMin){
      currMin = a[i];
    }
    else{
      ans += (currMin - a[i]);
    }
  }
  cout<<ans;
  return 0;
}
