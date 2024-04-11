from collections import Counter


class Solution:
    """
    Use a hashmap to keep track of the number of occurrences. Then just check
    if the number of occurrences is unique with a set.

    Time: O(n)
    Space: O(n)
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)

        seen = set()
        for v in counts.values():
            if v in seen:
                return False
            seen.add(v)

        return True
