class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s){
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
                continue;
            }
            if (c == ')'){
                if (st.empty() || st.top() != '(') return false;
                st.pop();
                continue;
            }
            if (c == ']'){
                if (st.empty() || st.top() != '[') return false;
                st.pop();
                continue;
            }
            if (c == '}'){
                if (st.empty() || st.top() != '{') return false;
                st.pop();
                continue;
            }
        }
        return st.empty();
    }
};