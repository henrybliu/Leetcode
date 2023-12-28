class Solution:
    '''
    We can use DP to reuse the number of combinations we have seen so far if we
    were to split at an index. If we were to not create a pair, we would carry
    over the number of combinations calculated at the right. Otherwise, if were
    to create a pair, we would also need to add the number of combinations
    after the pair was formed.

    Time: O(n)
    Space: O(n)
    '''
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[-1] = 1

        for i in range(len(s)-1,-1,-1):
            # zero is invalid and must be paired with a leading 1 or 2
            if s[i]=='0':
                dp[i] = 0
            # we did not form a pair so the number of combos stays the same
            else:
                dp[i] = dp[i+1]

            # increase the number of combos if we can form a pair
            if i+1 < len(s) and (s[i] == '1' or (s[i]=='2' and s[i+1] in '0123456')):
                dp[i] += dp[i+2]

        return dp[0]