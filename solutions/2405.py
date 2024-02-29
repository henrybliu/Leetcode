class Solution:
    '''
    Use a sliding window to try to create unique substrings. If we come across
    a duplicate letter, start a new substring at that point.

    Time: O(n)
    Space: O(n)
    '''
    def partitionString(self, s: str) -> int:
        # we always start with 1 substring bc of the constraint s.length >= 1
        # we increment count to start a new substring when we have found a duplicate letter
        count = 1
        l = 0
        seen = set()
        
        for r in range(len(s)):
            # if there is a repeated character, start a new substring
            if s[r] in seen:
                seen = set()
                count += 1
                l = r
            seen.add(s[r])

        return count