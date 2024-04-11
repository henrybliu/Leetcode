from collections import Counter


class Solution:
    """
    A word that appears exactly once in one of the sentences and doesn't appear
    in the other sentence is the same as the word occurring only once in the
    combination of both sentences.

    Time: O(n)
    Space: O(n)
    """

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        bothStrings = s1.split(" ") + s2.split(" ")
        bothCounts = Counter(bothStrings)

        res = []

        for k, v in bothCounts.items():
            if v == 1:
                res.append(k)

        return res
