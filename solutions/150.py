class Solution:
    """
    Use a stack to keep track of numbers before and after calculations.

    Time: O(n)
    Space: O(n)
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "-" or token == "*" or token == "+" or token == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == "-":
                    stack.append(str(num1 - num2))
                elif token == "+":
                    stack.append(str(num1 + num2))
                elif token == "/":
                    stack.append(int(num1 / num2))
                elif token == "*":
                    stack.append(int(num1 * num2))
            else:
                stack.append(token)

        return int(stack[0])
