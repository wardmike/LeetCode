// Prompt: https://leetcode.com/problems/delete-node-in-a-linked-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Runtime: 12 ms, faster than 100.00% of C++ online submissions for Delete Node in a Linked List.
// Memory Usage: 9.3 MB, less than 5.06% of C++ online submissions for Delete Node in a Linked List.
class Solution {
public:
    void deleteNode(ListNode* node) {
        // we "delete" this node by setting it's value equal to the next one
        // and deleting the next one
        node->val = node->next->val;
        ListNode* temp = node->next;
        node->next = node->next->next;
        delete temp;
    }
};
