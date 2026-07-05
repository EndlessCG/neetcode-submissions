class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_to_r, r_to_l = [nums[0]], [nums[-1]]
        for i in range(len(nums) - 1):
            l_to_r.append(l_to_r[i] * nums[i+1])
            r_to_l.append(r_to_l[i] * nums[-i-2])
        ret = []
        r_to_l = r_to_l[::-1]
        print(l_to_r, r_to_l)
        for i in range(len(nums)):
            left = l_to_r[i-1] if i > 0 else 1
            right = r_to_l[i+1] if i < len(nums) - 1 else 1
            ret.append(left * right)
        return ret