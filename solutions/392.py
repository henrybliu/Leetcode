class Solution:
    '''
    For s to be a subsequence of t, s cannot be larger than t. Loop through
    the indices of t and if the index value of s matches, increment the s
    index. At no point should the s index be larger than the lenght of s.

    Time: O(n)
    Space: O(n)
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if len(s) == 0 and len(t) > 0:
            return True

        if not s and not t:
            return True
        
        sIdx = 0
        for tIdx in range(len(t)):
            if t[tIdx] == s[sIdx]:
                sIdx += 1

            if sIdx >= len(s):
                return True

        return False