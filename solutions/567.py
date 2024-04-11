class Solution:
    """
    Create an array indexed by the lowercase characters starting from ord('a').
    Use a sliding window approach on s2 to compare with s1. We only compare
    the same number of letters in s2 as the length of s1.

    Time: O(n)
    Space: O(n)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # can create two arrays of the alphabet--where each index corresponds to the letter
        str1 = [0 for i in range(26)]
        str2 = [0 for i in range(26)]

        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]

            str1[ord(char1) - ord("a")] += 1
            str2[ord(char2) - ord("a")] += 1

        if str1 == str2:
            return True

        # remove and add letters in str2 to see if it matches str1
        # remove from left side, add to the right side
        l = 0
        for r in range(len(s1), len(s2)):
            charL = s2[l]
            charR = s2[r]

            str2[ord(charL) - ord("a")] -= 1
            str2[ord(charR) - ord("a")] += 1
            l += 1

            if str1 == str2:
                return True
        return False
