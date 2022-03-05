class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        bool flag=0;   // nếu flag == 1 thì tập con thỏa mãn y/c
        int n=nums.size();
        if(n<3)return 0;
        int ans=0;
        for (int len = 3; len <= n; len++)
        {   
            for (int i = 0; i <= n - len; i++)  // i : vị trí bất đầu của dãy con
            {
                flag=1;  
                int j = i + len - 1;  // j : vị trí kết thúc của dãy con         
                for (int k = i; k <= j-2; k++)
                {
                    if((nums[k]-nums[k+1])!=(nums[k+1]-nums[k+2]))
                    {
                        flag=0;   // flag == 0: dãy con không thỏa mãn y/c
 
                        break; 
                    }
                }
                if(flag)ans++;
            }
        }
        return ans;
    }
};
