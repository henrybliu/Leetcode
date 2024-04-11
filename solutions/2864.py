from collections import Counter


class Solution:
    """
    We always want to use 1 in the LSB to make the binary number odd. The rest
    of the 1s should go at the start of the binary string to increase the size
    of the number.

    Time: O(n)
    Space: O(n)
    """

    def maximumOddBinaryNumber(self, s: str) -> str:
        counts = Counter(s)
        numOnes = counts["1"]

        if numOnes == 0:
            return s

        res = ["0" for _ in range(len(s))]
        numOnes -= 1
        res[-1] = "1"

        for i in range(numOnes):
            res[i] = "1"

        return "".join(res)
