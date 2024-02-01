class Solution:
    '''
    Use DP to consider at the indices r and c, what is the longest subsequence
    that we can create at up to index r in text2 and up to index c in text1? We
    want to keep passing forward and down the maximum occurrences we have
    encountered so far. We know that all subsequences created after a match
    will use the previous match's length.   

    example:
    text1 = abcde
    text2 = ace

    DP array:
    x _ a b c d e
    _ 0 0 0 0 0 0
    a 0 1 1 1 1 1
    c 0 1 1 2 2 2
    e 0 1 1 2 2 3

    Notice that for a match, all later subsequences that can be formed will use that initial match. 

    Time: O(n*m)
    Space: O(n*m)
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create the DP array
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        rows = len(text2)+1
        cols = len(text1)+1

        for r in range(1,rows):
            for c in range(1,cols):
                if text1[c-1] == text2[r-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])

        return dp[-1][-1]