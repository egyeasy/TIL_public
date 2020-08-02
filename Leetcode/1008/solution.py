from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def search_and_build(current: TreeNode, search_node: TreeNode):
    if search_node.val < current.val:
        if not current.left:
            current.left = search_node
        else:
            search_and_build(current.left, search_node)
    else:
        if not current.right:
            current.right = search_node
        else:
            search_and_build(current.right, search_node)
            

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        
        N = len(preorder)
        
        for i in range(1, N):
            new_node = TreeNode(preorder[i])
            search_and_build(root, new_node)
        
        return root

sol = Solution()
sol.bstFromPreorder([8,5,1,7,10,12])