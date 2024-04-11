class Solution:
    """
    The key realization is that we can disregard the occurrences of 'X' and
    that 'L' can only move left and that 'R' can only move right. This means
    that for each 'R' in start should occur at an earlier index that each 'R'
    in end and similar logic applies for 'L'.

    Time: O(n)
    Space: O(1)
    """

    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if len(start) == 1 and len(end) == 1 and start != end:
            return False

        startIdx = 0
        endIdx = 0

        while startIdx < len(start) or endIdx < len(end):
            while startIdx < len(start) and start[startIdx] == "X":
                startIdx += 1
            while endIdx < len(end) and end[endIdx] == "X":
                endIdx += 1

            if endIdx == len(end) and startIdx == len(start):
                return True

            if endIdx == len(end) or startIdx == len(start):
                return False

            if end[endIdx] != start[startIdx]:
                return False

            if start[startIdx] == "R" and startIdx > endIdx:
                return False
            if start[startIdx] == "L" and startIdx < endIdx:
                return False

            startIdx += 1
            endIdx += 1
        return True
