from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        freq = [[] for i in range(len(nums))]
        for key, v in d.items():
            freq[v - 1].append(key)
        output_ls = []
        i = len(nums) - 1
        while len(output_ls) < k:
            if len(freq[i]) <= k - len(output_ls):
                output_ls.extend(freq[i])
            else:
                output_ls.extend(freq[i][:k - len(output_ls)])
            i -= 1
        return output_ls