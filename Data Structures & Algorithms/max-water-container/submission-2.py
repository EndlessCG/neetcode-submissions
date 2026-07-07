class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_vol = -1
        while i < j:
            cur = min(heights[i], heights[j]) * (j - i)
            max_vol = max(max_vol, cur)
            if heights[j] >= heights[i]:
                i += 1
            else:
                j -= 1
        return max_vol
