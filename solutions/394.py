class Solution:
    """
    Keep a stack to create encountered characters. When encountering a "]", recreate the operation that will multiply a single or group of characters a number of times.

    Time: O(n)
    Space: O(n)
    """

    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)

            else:
                currString = ""
                # keep popping until encountering a [
                while stack[-1] != "[":
                    currString = stack.pop() + currString

                stack.pop()
                numString = ""
                while stack and stack[-1].isdigit():
                    numString = stack.pop() + numString

                num = int(numString)

                stack.append(num * currString)

        return "".join(stack)
