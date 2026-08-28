# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def rec(root):
            if root is None:
                return 0
            nonlocal is_balanced
            if root.left:
                l_height = rec(root.left) + 1
            else:
                l_height = 0
            if root.right:
                r_height = rec(root.right) + 1
            else:
                r_height = 0
            if abs(l_height - r_height) > 1:
                is_balanced = False
            print(root.val, l_height, r_height)
            return max(l_height, r_height)
        rec(root)
        return is_balanced
        