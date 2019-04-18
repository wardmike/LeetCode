// Prompt: https://leetcode.com/problems/reverse-linked-list
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// recursive approach
// Runtime: 12 ms, faster than 42.90% of C++ online submissions for Reverse Linked List.
// Memory Usage: 9.4 MB, less than 5.07% of C++ online submissions for Reverse Linked List.
#include <queue>
class Solution {
private:
    std::queue<int> valQueue;
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) {
            return NULL;
        }
        valQueue.push(head->val);
        ListNode* prev = reverseList(head->next);
        ListNode* next = new ListNode(valQueue.front());
        valQueue.pop();
        next->next = prev;
        return next;   
    }
};
