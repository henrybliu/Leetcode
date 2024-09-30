class CustomStack:
    """
    Initialize the stack to be of size maxSize. This ensures that the only O(n)
    operation is for when initializing.

    - push is O(1)
    - pop is O(1)
    - increment is O(k), where k is the number of elements to increment
    """

    def __init__(self, maxSize: int):
        self.stack = [-1 for _ in range(maxSize)]
        self.idx = -1
        self.maxSize = maxSize - 1

    def push(self, x: int) -> None:
        if self.idx + 1 <= self.maxSize:
            self.idx += 1
            self.stack[self.idx] = x

    def pop(self) -> int:
        if self.idx < 0:
            return -1
        else:
            val = self.stack[self.idx]
            self.stack[self.idx] = -1
            self.idx -= 1
            return val

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.idx + 1)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
