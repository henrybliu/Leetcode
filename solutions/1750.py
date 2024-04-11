class Solution:
    """
    Can use two pointers to keep moving inwards so long that the pointers are
    pointing to the same characters on both ends.

    Time: O(n)
    Space: O(n)
    """

    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l < r and s[l] == s[r]:
            matching = s[l]

            # set to l <= r to prevent overlapping of l and r
            while l <= r and s[l] == matching:
                l += 1
            while r >= l and s[r] == matching:
                r -= 1

        return r - l + 1
