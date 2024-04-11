class Solution:
    """
    Create an array for each string where the ASCII value from lowercase 'a'
    is the index value. Compare these two arrays created.

    Time: O(n)
    Space: O(n)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        alpha1 = [0 for _ in range(26)]
        alpha2 = [0 for _ in range(26)]

        for c in s:
            alpha1[ord(c) - ord("a")] += 1

        for c in t:
            alpha2[ord(c) - ord("a")] += 1

        return alpha1 == alpha2
