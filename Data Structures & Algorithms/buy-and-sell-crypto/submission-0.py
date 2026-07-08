class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_v = prices[0]
        for v in prices:
            min_v = min(min_v, v)
            max_p = max(v - min_v, max_p)
        return max_p