class Node:
    """
    Description
    Creates and manipulates nodes

    Methods
    __init__(self, value): Creates node objects with data of value
    getData(self): returns data
    getNext(self): traverses to next node
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

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

    def insert(self, value=None):
        node = Node(value)
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

    def append(self, value):
        node = Node(value)
        current = self.head
        if current == None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        node = Node(newVal)
        current = self.head
        if current == None:
            self.head = node
        elif current.data is value:
            self.insert(newVal)
        else:
            while current != None:
                if current.next.data == value:
                    node.next = current.next
                    current.next = node
                    break
                else:
                    current = current.next

    def insertAfter(self, value, newVal):
        current = self.head
        while current:
            if current.data == value:
                node = Node(newVal, current.next)
                current.next = node
                return
            current = current.next
        return 'Target value not in list.'

    def delete(self, value):
        current = self.head
        if current == None:
            print('No nodes in list.')
        elif current.data is value:
            self.head = current.next
        else:
            while current.next.data != value:
                current = current.next
            current.next = current.next.next

    def kthFromEnd(self, k):
        # node_list = []
        # current = self.head

        # while current != None:
        #     node_list.append(current.data)
        #     current = current.next
        # if abs(k) > len(node_list):
        #     return 'Index value greater than list length.'
        # if k < 0:
        #     return node_list[abs(k)]
        # else:
        #     return node_list[len(node_list) - k - 1]
        head_start = 0
        follower = None
        leader = self.head
        while leader:
            leader = leader.next
            if follower:
                follower = follower.next
            elif head_start == k:
                follower = self.head
            else:
                head_start += 1
        if not follower:
            return 'Target index value greater than list length.'
        return follower.data

    def __str__(self):
        current = self.head
        node_list = []
        node_output = ''
        while current != None:
            node_list.append(f'{ {current.data} } -> ')
            current = current.next
        node_list.append('NULL')
        for node in node_list:
            node_output += node
        return node_output
