class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head) return NULL;
        Node* ptr = head;
        Node* newH = new Node(0);
        Node* newptr = newH;
        while(ptr){
            newptr->next = new Node(ptr->val);
            m[ptr] = newptr->next;
            ptr = ptr->next;
            newptr = newptr->next;
        }
        ptr = head;
        while(ptr){
            if (ptr->random){
                m[ptr]->random = m[ptr->random];
            } 
            ptr = ptr->next;
        }
        return newH->next;
    }
private:
    unordered_map<Node*, Node*> m;
};
