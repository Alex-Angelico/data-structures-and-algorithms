class InvalidOperationError(BaseException):
    pass


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


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next


class Stack:
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError(
                'Method not allowed on empty collection')
        node = self.top
        self.top = self.top.next
        return node.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError(
                'Method not allowed on empty collection')
        return self.top.value


class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty queue.')
        node = self.front
        self.front = self.front.next
        return node.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty queue.')
        return self.front.value
