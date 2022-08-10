class MyStack:

    def __init__(self):
        self.queues = []

    def push(self, x: int) -> None:
        self.queues.append(x)
        return self.queues

    def pop(self) -> int:
        val = self.queues[-1]
        self.queues = self.queues[:-1]
        return val

    def top(self) -> int:
        return self.queues[-1]

    def empty(self) -> bool:
        return True if not self.queues else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()