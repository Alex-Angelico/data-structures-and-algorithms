from linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
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
            return None

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


def repeat_checker(string, hashtable):
    string = string.casefold()
    word_list = string.split(' ')
    for i, item in enumerate(word_list):
        if not item.isalpha():
            word_list[i] = [
                character for character in item if character.isalpha()]
            word_list[i] = ''.join(word_list[i])
        if not len(word_list[i]):
            word_list.pop(i)

    print(word_list)

    for word in word_list:
        if hashtable.contains(word):
            return word
        hashtable.add(word, word)

    return None


if __name__ == '__main__':

    test_hashtable = Hashtable()

    test_string = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    repeated_word = repeat_checker(test_string, test_hashtable)
    print(repeated_word)
