class Solution:
    """
    Use a stack to keep track of the phrases that can be created. In 2 passes,
    we first prioritize the substring that is worth more points. Then, we pass
    through again to create the second substring.

    Time: O(n)
    Space: O(n)
    """

    def maximumGain(self, s: str, x: int, y: int) -> int:
        # remove phrase that is worth more points first
        firstWord, secondWord = "ab", "ba"
        firstPoints, secondPoints = x, y

        if y > x:
            firstWord, secondWord = "ba", "ab"
            firstPoints, secondPoints = y, x

        substrings = [firstWord, secondWord]
        phrasePoints = [firstPoints, secondPoints]
        res = 0

        stack = []
        for i, substring in enumerate(substrings):
            points = phrasePoints[i]
            for char in s:
                stack.append(char)
                if (
                    len(stack) >= 2
                    and stack[-2] == substring[0]
                    and stack[-1] == substring[1]
                ):
                    stack.pop()
                    stack.pop()
                    res += points

            s = "".join(stack)
            stack = []

        return res
