# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        value = 0

        def rec(node):
            nonlocal cnt, value
            # print(value, node.value)
            if node is None:
                return
            rec(node.left)
            cnt -= 1
            if cnt == 0:
                value = node.val
                return
            rec(node.right)
        rec(root)
        return value