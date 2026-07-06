class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        seen = set()
        max_cnt = 0
        for n in nums:
            if n in seen:
                continue
            i = n
            cnt = 0
            while i in s:
                cnt += 1
                i += 1
                max_cnt = max(max_cnt, cnt)
                seen.add(i)
        return max_cnt
