from collections import Counter


class Solution:
    """
    Use a dictionary to count the maximum frequency of any number. Then loop
    through the dictionary -- adding to the result if the number of occurrences
    matches the maximum frequency. This could be optimized to one pass.

    Time: O(n)
    Space: O(n)
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxFreq = max(counts.values())

        res = 0
        for k, v in counts.items():
            if v == maxFreq:
                res += v

        return res
