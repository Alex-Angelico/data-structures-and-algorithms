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

    def insert(self, value):
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
        current = self.head
        node = Node(value)
        if current == None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        current = self.head
        node = Node(newVal)
        # if current.data is value:
        #     self.insert(newVal)
        #     return

        if current == None:
            self.head = node
        else:
            while current != None:
                print(current.data)
                if current.next.data == value:
                    node.next = current.next.next
                    current.next = node
                    # current.next.next.data = value
                    # bumpvalue = value
                    # while current.next.next != None:
                    #     bumpvalue = value
                    #     value = current.next.next.data
                    #     current.next.next.data = bumpvalue
                    # current.next.next = Node(bumpvalue)
                    break
                    # current = current.next
                else:
                    current = current.next

            # while node.next != None:

        # current.next = node

        # while current != None:
        #     if current.next == None:
        #         node = self.head
        #         node.next = current
        #         break
        #     elif current.next.value == value:
        #         node.next = current.next
        #         curent.next = node
        #         break
        #     else:
        #         current = current.next

    def insertAfter(self, value, newVal):
        node = Node(newVal)
        current = self.head
        if self.head == None:
            return 'List is empty.'
        if self.head == value:
            current.next = node
        while current.next != value:
            current = current.next
        current.next.next = node

    def kthFromEnd(self, k):
        node_list = []
        current = self.head

        while current != None:
            node_list.append(current.data)
            current = current.next
        if abs(k) > len(node_list):
            return 'Index value greater than list length.'
        if k < 0:
            return node_list[abs(k)]
        else:
            return node_list[len(node_list) - k]

    def __str__(self):
        current = self.head
        node_list = []
        node_output = ''
        while current != None:
            node_list.append(f"{ {current.data} } -> ")
            current = current.next
        node_list.append('NULL')
        for node in node_list:
            node_output += node
        return node_output


llist = LinkedList()
llist.insert(23)
llist.insert(98)
llist.insert(415)
llist.insert(123)
llist.insert(981)
llist.insert(454)
llist.insert(213)
llist.insert(198)
llist.insert(455)
llist.insert(253)
llist.insert(978)
llist.insert(45)
llist.insert(203)
llist.insert(918)
llist.insert(45)


# x = llist.kthFromEnd(7)
# print(x)

llist.insertBefore(454, 69)

print(llist)

# print('test:', llist_empty)
