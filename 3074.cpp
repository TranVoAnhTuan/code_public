class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        long long s = 0;
        int a = 0;
        sort(capacity.begin(), capacity.end(), greater<int>());
        for(int v: apple){
            s += v;
        }
        for(int c: capacity){
            s -= c;
            a++;
            if(s <= 0){
                return a;
            }
        }
        return a;
    }
};
