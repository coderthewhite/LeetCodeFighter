class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        vector<int> a(7, 0), b(7, 0), c(7, 0);
        int len = tops.size();
        for (int i = 0; i < len; i++){
            int m = tops[i], n = bottoms[i];
            a[m]++;
            b[n]++;
            if (m == n) c[m]++;
        }
        
        int ans = len;
        for (int i = 1; i <= 6; i++){
            if (a[i] + b[i] - c[i] == len){
                int step = min(a[i], b[i]) - c[i];
                ans = min(ans, step);
            }
        }
        return ans == len ? -1 : ans;
    }
};