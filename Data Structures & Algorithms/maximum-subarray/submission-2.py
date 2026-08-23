class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max_prefix = -float('inf')
        global_max = -float('inf')
        for n in nums:
            cur_max_prefix = max(n, cur_max_prefix + n)
            global_max = max(cur_max_prefix, global_max)
        return global_max 