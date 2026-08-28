# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def rec(root, depth):
            print(root.val, depth)
            max_depth = depth
            if root.left:
                depth_l = rec(root.left, depth + 1)
                max_depth = max(max_depth, depth_l)
            if root.right:
                depth_r = rec(root.right, depth + 1)
                max_depth = max(max_depth, depth_r)
            return max_depth
        return 0 if root is None else rec(root, 1)
        