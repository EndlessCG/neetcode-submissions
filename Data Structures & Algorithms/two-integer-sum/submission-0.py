class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {}
        for i, n in enumerate(nums):
            if n in wanted:
                return [wanted[n], i]
            wanted[target - n] = i
        