# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

deepest_level = -1
leaf_dict = {}

def searchNode(node: TreeNode, level: int) -> None:
    global deepest_level, leaf_dict
    if not node.left and not node.right:
        if level > deepest_level:
            deepest_level = level
            leaf_dict[level] = [node.val]
        elif level == deepest_level:
            leaf_dict[level].append(node.val)
        return
    if node.left:
        searchNode(node.left, level + 1)
    if node.right:
        searchNode(node.right, level + 1)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        global deepest_level, leaf_dict
        deepest_level = -1
        leaf_dict = {}
        searchNode(root, 0)
        
        return sum(leaf_dict[deepest_level])