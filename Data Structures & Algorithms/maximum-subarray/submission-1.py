class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_prefix = [-float('inf') for _ in nums]
        max_prefix[0] = nums[0]
        for i in range(1, len(nums)):
            max_prefix[i] = max(nums[i], max_prefix[i - 1] + nums[i])
        return max(max_prefix)