class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_h, right_h = height[i], height[j]
        total_w = 0
        while i < j:
            if height[i] > height[j]:
                j -= 1
                right_h = max(right_h, height[j])
                total_w += max(min(left_h, right_h) - height[j], 0)
            else:
                i += 1
                left_h = max(left_h, height[i])
                total_w += max(min(left_h, right_h) - height[i], 0)
            # print(i, j, total_w, left_h, right_h)
        return total_w                 