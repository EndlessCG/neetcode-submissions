# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        def rec(root):
            if root.left is None and root.right is None:
                return 0
            nonlocal max_diam
            if root.left is None:
                l_max = 0
            elif root.left:
                l_max = rec(root.left) + 1
            if root.right is None:
                r_max = 0
            elif root.right:
                r_max = rec(root.right) + 1
            max_diam = max(max_diam, l_max + r_max)
            return max(l_max, r_max)
        rec(root)
        return max_diam
            