class Solution:
    '''
    Have a seen set to keep track of seen characters. Want to keep adding to
    the current length while the current character hasn't been seen yet.

    Time: O(n)
    Space: O(n)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        seen = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            length = max(length, len(seen))
            r+=1

        return length