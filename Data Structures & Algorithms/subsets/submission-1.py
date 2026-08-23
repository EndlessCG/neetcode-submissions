class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret_ls = []
        queue = [([], 1), ([nums[0]], 1)]
        while queue:
            ls, layer = queue.pop(0)
            if layer < len(nums):
                queue.extend([(ls, layer + 1), (ls + [nums[layer]], layer + 1)])
            else:
                ret_ls.append(ls)
        return ret_ls
