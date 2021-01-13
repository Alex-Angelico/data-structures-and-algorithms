class InvalidOperationError(BaseException):
    pass


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
                'Method not allowed on  empty colleciton')
        node = self.top
        self.top = self.top.next
        return node.value

    def is_empty(self):
        return True

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError(
                'Method not allowed on empty colleciton.')
        return self.top.value


class Queue:
    def __init__(self):
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
        return True

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty queue.')
        return self.front.value
