#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
ll t;
void solve(){
  ll n;
  cin >> n;
  string s;
  cin >> s;
  ll cnt = 0;
  for(char a: s){
    if(a == '1'){
      cnt++;
    }
  }
  if(cnt == 2 && s.find("11") != string::npos){
    cout << "NO" << '\n';
    return;
  }
  if(cnt & 1){
    cout << "NO" << '\n';
  } else{
    cout << "YES" << '\n';
  }
}
int main(){
  IOS;
  cin >> t;
  ll n;
  while(t--){
    solve();
  }

  return 0;
}

