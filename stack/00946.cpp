class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int i = 0;      // chạy trên mảng popped 
        stack<int> st;
        for (int x : pushed){
            st.push(x);
            while(!st.empty() && st.top() == popped[i]){ 
                st.pop();
                i++;
            }
        }
        return st.empty();
    }
};