class Node:
    """
    Description
    Creates and manipulates nodes

    Methods
    __init__(self, value): Creates node objects with data of value
    getData(self): returns data
    getNext(self): traverses to next node
    """

    def __init__(self, value=None):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class LinkedList:
    """
    Description
    Creates and manipulates linked lists of nodes

    Methods
    __init__(self, value): Creates empty linked lists
    insert(self, node): Adds a new node object to the start of a list
    includes(self, value): Checks if at least one node in a linked list contains a specified value
    __str__(self): Generates the linked values of a whole linked list object
    """

    def __init__(self):
        self.head = None

    def insert(self, node):
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current != None:
            if current.getData() == value:
                return True
            else:
                current = current.getNext()
        return False

    def __str__(self):
        current = self.head
        node_list = []
        node_output = ''
        while(current):
            node_list.append(f"{ {current.data} } -> ")
            current = current.next
            if current == None:
                node_list.append('NULL')
        for node in node_list:
            node_output += node
        return node_output
