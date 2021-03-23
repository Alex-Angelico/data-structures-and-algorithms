from linked_list import LinkedList


class Hashtable:
    def __init__(self, size=128):
        self._size = size
        # None can be replaced with LinkedList() at higher initial setup cost
        self._buckets = size * [None]

    def _hash(self, key):
        sum = 0
        for character in key:
            sum += ord(character)

        primed = sum * 599
        index = primed % self._size
        return index

    def add(self, key, value):
        hashed_key_index = self._hash(key)
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].append((key, value))

    def get(self, key):
        requested_key = self._hash(key)
        if self._buckets[requested_key]:
            current = self._buckets[requested_key].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
        else:
            return 'NULL'

    def contains(self, key):
        requested_key = self._hash(key)
        if self._buckets[requested_key]:
            current = self._buckets[requested_key].head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        else:
            return False
