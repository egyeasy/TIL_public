# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
way = ""

def searchNode(search_node: TreeNode, target_node: TreeNode, curr_way: str) -> None:
    global way
    if search_node == target_node:
        way = curr_way
        return
    if search_node.left:
        searchNode(search_node.left, target_node, curr_way + "l")
    if search_node.right:
        searchNode(search_node.right, target_node, curr_way + "r")

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        global way
        searchNode(original, target, "")
        
        cloned_target = cloned
        for direction in way:
            if direction == "l":
                cloned_target = cloned_target.left
            else:
                cloned_target = cloned_target.right
        return cloned_target