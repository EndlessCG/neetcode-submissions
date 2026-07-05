class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1 for _ in range(len(nums))]
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            ret[i] *= prod
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            ret[i] *= prod
        return ret