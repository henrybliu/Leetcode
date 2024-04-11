class Solution:
    """
    At each index, we want to try to create even and odd palindromes. For each
    one that we can create, increment the count.

    Time: O(n^2)
    Space: O(1)
    """

    def countSubstrings(self, s: str) -> int:
        res = 0
        # odd length palindromes
        i = 0
        while i < len(s):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            i += 1

        # even length palindromes
        i = 0
        while i < len(s):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            i += 1

        return res
