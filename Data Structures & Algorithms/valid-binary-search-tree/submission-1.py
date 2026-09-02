# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node, l, r):
            if node is None:
                return True
            if node.val >= r or node.val <= l:
                return False
            return rec(node.left, l, min(r, node.val)) and rec(node.right, max(l, node.val), r)
        return rec(root, -float('inf'), float('inf'))

        