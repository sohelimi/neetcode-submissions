class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        

    def push(self, x: int) -> None:
        self.stk1.append(x)
        

    def pop(self) -> int:
        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
        
        res = self.stk1.pop()

        while self.stk2:
            self.stk1.append(self.stk2.pop())
        return res

    def peek(self) -> int:
        while len(self.stk1) >1:
            self.stk2.append(self.stk1.pop())
        res = self.stk1[-1]

        while self.stk2:
            self.stk1.append(self.stk2.pop())
        return res

    def empty(self) -> bool:
        if not self.stk1:
            return True
        return False
        








'''
class MyQueue:
    def __init__(self):
        # stack1 stores the queue elements
        # stack2 is a temporary stack used when removing/peeking
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Add the new element to the back of the queue
        # Since we're using a stack, we just append it to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # We need to remove the front element of the queue.
        # Since the front is at the bottom of stack1,
        # move elements to stack2 until only the front element remains.
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        # Now the last element in stack1 is the front of the queue
        res = self.stack1.pop()

        # Move everything back so stack1 is restored
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res

    def peek(self) -> int:
        # Same idea as pop, but we only want to look at the front element
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        # The remaining element is the front of the queue
        res = self.stack1[-1]

        # Restore stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res

    def empty(self) -> bool:
        # Queue is empty if stack1 has no elements
        return not self.stack1
'''

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()