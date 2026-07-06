class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        i = 0
        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            n_target = nums[i]
            while j < k:
                s = nums[j] + nums[k] + n_target
                if s == 0:
                    answers.append([nums[j], nums[k], n_target])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # while k > j and nums[k] == nums[k + 1]:
                    #     k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            i += 1

        return answers
                