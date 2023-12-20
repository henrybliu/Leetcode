class Solution:
    '''
    Use a hashmap to keep track of the indices of where the gaps are. The 0 and
    the last indices are considered gaps.

    Time: O(n)
    Space: O(n)
    '''
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {0:0}

        for row in wall:
            row = row[:-1]
            currSum = 0
            for num in row:
                currSum += num
                gaps[currSum] = 1 + gaps.get(currSum, 0)

        return len(wall) - max(gaps.values())