class Solution:
    """
    O(n)
    --  use a helper function to calculate the value within parentheses once it
        is stripped
    --  have the main function check if the negative signs will affect the
        parsing
    """

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        # create the ongoing sum for values a string with no parentheses
        def noParen(s):
            currNum = ""
            operator = "+"
            currSum = 0

            for i, char in enumerate(s):
                if char.isdigit():
                    currNum += char
                else:
                    if operator == "+" and currNum:
                        currSum += int(currNum)
                    elif operator == "-" and currNum:
                        currSum += -int(currNum)
                    currNum = ""

                if char == "+":
                    operator = char
                elif char == "-":
                    operator = char

            if operator == "+" and currNum:
                currSum += int(currNum)
            elif operator == "-" and currNum:
                currSum += -int(currNum)

            return currSum

        # get rid of parentheses + parsing
        stack = []
        currNum = ""
        for char in s:
            if char.isdigit():
                currNum += char
            else:
                if currNum:
                    stack.append(currNum)
                    currNum = ""

                if char == ")":
                    toCalc = []
                    while stack and stack[-1] != "(":
                        toCalc.append(stack.pop())
                    stack.pop()

                    # check if the sign outside the parentheses is negative
                    # check if the value inside the parentheses is negative

                    isNegative = False
                    if stack and stack[-1] == "-":
                        isNegative = True

                    toCalc = toCalc[::-1]
                    res = noParen(toCalc)

                    if res < 0 and isNegative:
                        stack.pop()
                        stack.append("+")
                        stack.append(str(abs(res)))
                    elif res < 0 and not isNegative:
                        stack.append("-")
                        stack.append(str(abs(res)))
                    else:
                        stack.append(str(res))
                else:
                    stack.append(char)

        if currNum:
            stack.append(currNum)

        # add remaining items up
        return noParen("".join(stack))
