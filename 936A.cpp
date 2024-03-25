#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fr(a,b) for(long long a = 0; a < b; a++);
#define fd(a,b) for(long long a = b - 1; a >= 0; a--);
const int MAXN=2e5+5;
int n,a[MAXN];
void solve(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	sort(a+1,a+n+1);
	int cnt=0;
	for(int i=(n+1)/2;i<=n;i++) if(a[i]==a[(n+1)/2]) cnt++;
	cout<<cnt<<'\n';
}
int main(){
	ios::sync_with_stdio(false);
	// freopen("Otomachi_Una.in","r",stdin);
	// freopen("Otomachi_Una.out","w",stdout);
	int _;cin>>_;
	while(_--) solve();
	return 0;
}
