class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_l = 0
        cur_l = 0
        st = 0
        for i in range(len(s)):
            if s[i] in seen:
                # print(i, s[i], 'seen')
                st = max(st, seen[s[i]] + 1)
                cur_l = i - st + 1
            else:
                # print(i, s[i], 'unseen', cur_l + 1)
                cur_l += 1
            max_l = max(max_l, cur_l)
            seen[s[i]] = i

        return max_l