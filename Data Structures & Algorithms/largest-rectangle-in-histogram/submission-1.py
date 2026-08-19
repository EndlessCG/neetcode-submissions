class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_h = []
        max_a = -1
        for i, h in enumerate(heights):
            l_h = i
            while prev_h and h < prev_h[-1][1]:
                max_a = max(max_a, (i - prev_h[-1][0]) * prev_h[-1][1])
                l_h = prev_h[-1][0] if prev_h[-1][1] >= h else l_h
                prev_h.pop()
            prev_h.append((l_h, h))
        while prev_h:
            max_a = max(max_a, (len(heights) - prev_h[-1][0]) * prev_h[-1][1])
            prev_h.pop()
        return max_a



