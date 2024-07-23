from collections import Counter


class Solution:
    """
    First sort by magnitude of values to guarantee that we have ascending
    order. Then, sort the values by their frequency in descending order. The
    key note is that sorting in Python is stable. This means that if two
    elements are of the same value by the comparing function, they will
    maintain its original ordering.

    Time: O(nlogn)
    Space: O(n)
    """

    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        # put in descending order by number size -- guarantees that if values
        # have the same frequency, they will be in decreasing order
        nums.sort(key=lambda num: num, reverse=True)
        # put in ascending order by frequency -- sorting is stable, meaning
        # that if 2 elements are of the same value/magnitude, they remain in
        # existing order
        nums.sort(key=lambda num: counts[num])

        return nums
