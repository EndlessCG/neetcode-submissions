class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        if s[0] == '0':
            dp[0] = 0
            if len(dp) > 1:
                dp[1] = 0
        else:
            dp[0] = 1
            if len(dp) > 1 and s[1] != '0':
                dp[1] += 1
            if len(dp) > 1 and (s[0] == '0' or s[0] == '1' or (s[0] == '2' and '0' <= s[1] <= '6')):
                dp[1] += 1

        for i in range(2, len(s)):
            if i - 1 >= 0 and s[i] != '0':
                dp[i] += dp[i - 1]
            if i - 2 >= 0 and (s[i - 1] == '1' or s[i - 1] == '2' and '0' <= s[i] <= '6'):
                dp[i] += dp[i - 2]

        return dp[-1]