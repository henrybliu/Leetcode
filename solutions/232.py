class MyQueue:
    '''
    Use two stacks to implement a FIFO queue using only stack operations. 

    Stack1's last element to be popped is the element at the front of the
    queue.

    Stack2 allows us to save the contents of the rest of the queue. We need to
    move these items back into stack1 after finding the first element.

    Time: O(n) for pop and peek. O(1) for init, push, and empty
    Space: O(n) 
    '''

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        front = self.stack1.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return front 

    
    def peek(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        front = self.stack1.pop()

        self.stack1.append(front)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return front

    def empty(self) -> bool:
        return len(self.stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()