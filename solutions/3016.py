from collections import Counter


class Solution:
    """
    Want the most common letters to be assigned first so that they have less clicks
    """

    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        order = list(count.keys())
        order.sort(key=lambda letter: count[letter], reverse=True)

        mapping = {}
        for i in range(len(order)):
            mapping[order[i]] = i // 8 + 1

        res = 0
        for letter in word:
            res += mapping[letter]

        return res
