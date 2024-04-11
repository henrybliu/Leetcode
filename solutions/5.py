class Solution:
    """
    Can expand from a center point to try and create even and odd length
    palindromes.

    Time: O(n^2)
    Space: O(1)
    """

    def longestPalindrome(self, s: str) -> str:
        res = ""
        resCount = 0

        for i in range(len(s)):
            # test for even length palindromic substrings
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resCount:
                    res = s[l : r + 1]
                    resCount = r - l + 1

                l -= 1
                r += 1

            # test for odd length palindromic substrings
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resCount:
                    res = s[l : r + 1]
                    resCount = r - l + 1

                l -= 1
                r += 1

        return res
