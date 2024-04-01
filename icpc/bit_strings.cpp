#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
int main() {
    IOS;
    ll n, answer = 1;
    cin >> n;
    fi(i, 0, n - 1){
        answer *= 2;
        answer %= MOD;
    }
    cout << answer;
}
