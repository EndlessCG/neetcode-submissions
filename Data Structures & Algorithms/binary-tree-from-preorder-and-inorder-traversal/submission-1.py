# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_i = 0
        inorder_d = {}
        for i, v in enumerate(inorder):
            inorder_d[v] = i

        def rec(node, in_l, in_i, in_r):
            nonlocal preorder_i, inorder_d
            if in_l == in_r:
                return
            preorder_i += 1
            if in_l != in_i:
                left = TreeNode(preorder[preorder_i])
                node.left = left
                rec(left, in_l, inorder_d[left.val], in_i)
            if in_i != in_r - 1:
                right = TreeNode(preorder[preorder_i])
                node.right = right
                rec(right, in_i + 1, inorder_d[right.val], in_r)

        root = TreeNode(preorder[0])
        rec(root, 0, inorder.index(root.val), len(inorder))
        return root

        