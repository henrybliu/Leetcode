from collections import defaultdict


class Solution:
    """
    Count the number of occurrences of each letter in order. If a letter in s
    is not in order, just add it to a miscellaneous string that will be added
    to the end of the result. Loop through the letters in order and add the
    number of occurrences of that letter in s.

    Time: O(n)
    Space: O(n)
    """

    def customSortString(self, order: str, s: str) -> str:
        orderSet = set(order)
        counts = defaultdict(int)
        misc = ""

        for l in s:
            if l in orderSet:
                counts[l] += 1
            else:
                misc += l

        res = ""
        for l in order:
            res += l * counts[l]

        return res + misc
