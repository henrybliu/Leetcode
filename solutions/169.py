from collections import defaultdict


class Solution:
    """
    We can do this in one pass by updating the count of each value's number of
    occurrences and checking if that is the greatest occurrence.

    Time: O(n)
    Space: O(n)
    """

    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        resCount = 0

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if counts[num] > resCount:
                resCount = counts[num]
                res = num

        return res
