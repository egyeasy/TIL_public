#include <queue>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        long long int sum = 0;
        std::queue<TreeNode*> q;
        if (root != nullptr) {
            q.push(root);    
        }
        TreeNode* curr = root;
        //std::cout << "SUM : " << sum << std::endl;
        while (!q.empty()) {
            curr = q.front();
            q.pop();
            //std::cout << "VISITED : " << curr->val << std::endl;
            if (L <= curr->val && curr->val <= R) {
                //std::cout << "ADD : " << curr->val << std::endl;
                sum += curr->val;
            }
            if (curr->left != nullptr)
                q.push(curr->left);
            if (curr->right != nullptr)
                q.push(curr->right);
        }
        //std::cout << "SUM : " << sum << std::endl;
        
        return sum;
    }
};