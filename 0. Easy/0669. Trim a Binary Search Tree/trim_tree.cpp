// Prompt: https://leetcode.com/problems/trim-a-binary-search-tree
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Runtime: 28 ms, faster than 43.10% of C++ online submissions for Trim a Binary Search Tree.
// Memory Usage: 22.1 MB, less than 23.66% of C++ online submissions for Trim a Binary Search Tree.
#include <queue>
class Solution {
public:
    void findNodesWithinRange(TreeNode* node, int L, int R, std::queue<int>& keep) {
        if (node != NULL) {
            if (node->val <= R && node->val >= L) {
                keep.push(node->val);
                findNodesWithinRange(node->left, L, R, keep);
                findNodesWithinRange(node->right, L, R, keep);
            } else if (node->val > R) {
                findNodesWithinRange(node->left, L, R, keep);
            } else if (node->val < L) {
                findNodesWithinRange(node->right, L, R, keep);
            }
        }
    }
    void addNode(TreeNode* root, int val) {
        if (root->val < val) {
            if (root->right == NULL) {
                root->right = new TreeNode(val);
            } else {
                addNode(root->right, val);                
            }
        } else {
            if (root->left == NULL) {
                root->left = new TreeNode(val);
            } else {
                addNode(root->left, val);                
            }
        }
    }
    
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        std::queue<int> nodesToKeep;
        findNodesWithinRange(root, L, R, nodesToKeep);
        // add them to a tree
        if (!nodesToKeep.empty()) {
            TreeNode* newTree = new TreeNode(nodesToKeep.front());
            nodesToKeep.pop();
            while (!nodesToKeep.empty()) {
                addNode(newTree, nodesToKeep.front());
                nodesToKeep.pop();
            }
            return newTree;
        } else {
            return NULL;
        }
    }
};
