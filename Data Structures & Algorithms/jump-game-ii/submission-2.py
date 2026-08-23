class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        cur_farthest = 0
        steps = 0
        for i in range(len(nums)):
            if i > cur_farthest:
                cur_farthest = farthest
                steps += 1
            if i + nums[i] > farthest:
                farthest = i + nums[i]
            
        return steps