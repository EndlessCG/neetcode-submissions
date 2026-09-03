# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = [root]
        encoded = ""
        while queue:
            node = queue.pop(0)
            if node is None:
                encoded += "*#"
                continue
            encoded += f"{node.val}#"
            queue.append(node.left)
            queue.append(node.right)
        print(encoded)
        return encoded[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split('#')
        if vals[0] == '*':
            return None
        root = TreeNode(vals[0])
        queue, next_queue = [[root, 0]], []
        for v in vals[1:]:
            # print(v, [(n[0].val, n[1]) for n in queue], [(n[0].val, n[1]) for n in next_queue])
            # if len(queue) == 0 and len(next_queue),
            if len(queue) == 0 and len(next_queue) != 0:
                queue, next_queue = next_queue, []
            
            cur_parent, kids = queue[0]
            if v != '*':
                node = TreeNode(v)
                next_queue.append([node, 0])
            if kids == 0:
                if v != '*':
                    cur_parent.left = node
                queue[0][1] += 1
            elif kids == 1:
                if v != '*':
                    cur_parent.right = node
                queue.pop(0)
        return root
                
