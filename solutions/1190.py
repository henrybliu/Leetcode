class Solution:
    """
    Use a stack to keep track of the indices of opening parentheses. When
    encountering a closing parenthesis, reverse the contents between the
    parentheses pair.

    Time: O(n^2) bc of splicing
    Space: O(n)
    """

    def reverseParentheses(self, s: str) -> str:
        stack = []

        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                startIdx = stack.pop()
                # reverse that section of the string and update s
                # we cannot remove the parentheses yet because of how we index s
                s = s[:startIdx] + s[startIdx : idx + 1][::-1] + s[idx + 1 :]

        # remove any parentheses in the final result
        return "".join([ch for ch in s if ch not in "()"])
