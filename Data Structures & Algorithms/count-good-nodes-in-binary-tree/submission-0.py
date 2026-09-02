# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def rec(node, cur_max):
            if node is None:
                return
            # print(node.val, cur_max)
            nonlocal good_nodes
            if node.val >= cur_max:
                good_nodes += 1
                cur_max = node.val
                
            rec(node.left, cur_max)
            rec(node.right, cur_max)
        rec(root, -101)
        return good_nodes