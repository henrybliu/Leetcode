from collections import defaultdict


class Solution:
    """
    Treat this problem like two-sum. We can have a dictionary that keeps track
    of the count of the occurrences per number. We should also realize that at
    most, we will have 2^20 + 2^20 -- meaning that our largest number is 2^21.
    To prevent double counting pairs, we can also update a value's number of
    occurrences only when iterating over it.

    """

    def countPairs(self, deliciousness: List[int]) -> int:
        counts = defaultdict(int)
        modulo = 10**9 + 7
        res = 0

        for d in deliciousness:
            for i in range(22):
                if 2**i - d in counts:
                    res += counts[2**i - d]
            counts[d] += 1

        return res % modulo
