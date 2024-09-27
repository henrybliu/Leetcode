class Solution:
    """
    Can use bitmasking to keep track of the counts of each of the vowels. We
    can use binary to represent the count of a vowel (even or odd). Keep track
    of the index at that mask and if the mask appears again, it means that we
    have found another vowel to satisfy the even count.
    """

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        mask = 0
        dp = {0: -1}
        res = 0

        for i, c in enumerate(s):
            if c in vowels:
                # add a 1 for the case when c is a
                mask = mask ^ (1 + ord(c) - ord("a"))
            if mask in dp:
                res = max(res, i - dp[mask])
            else:
                dp[mask] = i

        return res
