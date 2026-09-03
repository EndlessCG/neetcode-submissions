# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def rec(node):
            if node is None:
                return -1
            nonlocal max_sum
            left_max = max(rec(node.left), 0)
            right_max = max(rec(node.right), 0)
            cur_sum = left_max + node.val + right_max
            # print(node.val, left_max, right_max, cur_sum)
            max_sum = max(max_sum, cur_sum)
            return max(left_max, right_max) + node.val
        rec(root)
        return max_sum