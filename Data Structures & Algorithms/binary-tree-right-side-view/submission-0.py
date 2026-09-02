# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [(root, 0)]
        ordered_ls = []
        while queue:
            node, height = queue.pop(0)
            if node is None:
                continue
            if len(ordered_ls) <= height:
                ordered_ls.append([])
            ordered_ls[height].append(node.val)
            queue.append((node.left, height + 1))
            queue.append((node.right, height + 1))
        return [l[-1] for l in ordered_ls]       