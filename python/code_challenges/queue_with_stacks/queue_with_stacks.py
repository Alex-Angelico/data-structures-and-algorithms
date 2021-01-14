from stacks_and_queues import Node, Stack, InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.read_stack = Stack()
        self.hold_stack = Stack()

    def enqueue(self, value):
        self.read_stack.push(value)

    def dequeue(self):
        current = self.read_stack.top
        while current.next:
            node = self.read_stack.pop()
            self.hold_stack.push(node)
            current = current.next
        front = self.read_stack.pop()

        current = self.hold_stack.top
        while current:
            node = self.hold_stack.pop()
            self.read_stack.push(node)
            current = current.next
        return front


# x = PseudoQueue()

# x.enqueue(5)
# x.enqueue(10)
# x.enqueue(15)
# x.enqueue(20)

# y = x.dequeue()
# x.dequeue()
# x.dequeue()
# z = x.dequeue()

# print(y, z)
