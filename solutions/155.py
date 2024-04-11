class MinStack:
    """
    Can retrieve the minimum value in constant time by using another stack that
    maintains the minimum value seen so far.

    Time: O(1)
    Space: O(n)
    """

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        self.minStack.pop()
        return self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
