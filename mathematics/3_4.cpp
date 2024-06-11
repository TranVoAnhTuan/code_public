#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
int main(){
  IOS;
  freopen("test.inp", "r", stdin);
  freopen("test.out", "w", stdout);
  ll n;
  cin >> n;
  float y[20], x[20];
  fi(i,1,n){
    cin >> y[i];
    // y[i] -= 7;
  }
  fi(i, 1, n){
    cin >> x[i];
    // x[i] -= 14;
  }
  float _x = 0, _y = 0;
  fi(i, 1, n){
    _y += y[i]/n;
    _x += x[i]/n;
  }
  float ssy = 0, ssx =0, sxy = 0;
  fi(i, 1, n){
    sxy += (x[i]-_x)*(y[i]-_y);
    ssx += (x[i]-_x)*(x[i]-_x);
    ssy += (y[i]-_y)*(y[i]-_y);
  }
  float b1 = sxy/ssx ;
  float b0 = _y - (sxy/ssx)*_x ;
  float e[20], sse = 0;
  fi(i, 1, n){
    e[i] = y[i] - b0 - b1*x[i];
    sse += (e[i]*e[i]);
  }
  cout << b1 << '\t' << b0 << '\t' << sqrt(sse/(n-2));
  return 0;
}

