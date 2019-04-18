// Prompt: https://leetcode.com/problems/reverse-linked-list
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// iterative approach
// Runtime: 12 ms, faster than 42.90% of C++ online submissions for Reverse Linked List.
// Memory Usage: 9.4 MB, less than 5.07% of C++ online submissions for Reverse Linked List.
#include <vector> 
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        std::vector<int> valsStack;
        while (head != NULL) {
            valsStack.push_back(head->val);
            head = head->next;
        }
        ListNode* reversedHead = new ListNode(valsStack.back());
        valsStack.pop_back();
        ListNode* iterator = reversedHead;
        while (valsStack.size() > 0) {
            iterator->next = new ListNode(valsStack.back());
            valsStack.pop_back();
            iterator = iterator->next;
        }
        return reversedHead;
    }
};
