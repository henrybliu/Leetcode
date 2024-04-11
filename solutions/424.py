from collections import defaultdict


class Solution:
    """
    Keep track of the maximum count of the same characters for a given
    substring. The length of the current substring added to the count of the
    most common character acts as having replaced a character k times.

    Time: O(n)
    Space: O(n)
    """

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)
        length = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            # if window has too many letters that you can't replace, then you need to decrease the window size
            while (r - l + 1) > (max(counts.values()) + k):
                counts[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)

        return length
