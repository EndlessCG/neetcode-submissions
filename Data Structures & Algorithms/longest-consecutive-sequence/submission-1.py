class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_cnt = 0
        for n in nums:
            if n - 1 not in s:
                i = n
                cnt = 0
                while i in s:
                    cnt += 1
                    i += 1
                    max_cnt = max(max_cnt, cnt)
        return max_cnt
