from collections import Counter, defaultdict


class Solution:
    """
    Use bucket sort to group values by their number of appearances. This works
    because a number can only appear at max the length of the input string.

    Time: O(n)
    Space: O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        groups = defaultdict(list)
        for key, value in counts.items():
            groups[value].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            if i in groups:
                for v in groups[i]:
                    if len(res) == k:
                        return res
                    res.append(v)
        return res
