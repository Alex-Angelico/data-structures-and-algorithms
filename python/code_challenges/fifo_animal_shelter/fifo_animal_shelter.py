# from stacks_and_queues import Node, InvalidOperationError


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next


class AnimalShelter:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value=None):
        animal = Node(value.lower())
        if self.front is None:
            self.front = animal
            self.rear = animal
        else:
            self.rear.next = animal
            self.rear = animal

    def dequeue(self, pref=None):
        if pref is None:
            return self.front.value
        pref = pref.lower()
        if pref != 'cat' and pref != 'dog':
            return None
        else:
            current = self.front
            while current.value != pref:
                current = current.next
            return current.value


x = AnimalShelter()

x.enqueue('cat')
x.enqueue('dog')
x.enqueue('dog')

y = x.dequeue('MONKEY')

print(x.front.value, y)
