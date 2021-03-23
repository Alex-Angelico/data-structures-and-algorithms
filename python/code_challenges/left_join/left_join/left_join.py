# from left_join.linked_list import LinkedList
from hashtable import Hashtable


def left_joiner(left, right):
    joined_data = []
    for bucket in left._buckets:
        if bucket:
            current = bucket.head
            while current:
                left_column = [current.data[0], current.data[1]]
                right_value = right.get(current.data[0])
                left_column.append(right_value)
                current = current.next
            joined_data.append(left_column)
    return joined_data


if __name__ == '__main__':

    hashmap1 = Hashtable()
    hashmap2 = Hashtable()

    hashmap1.add('fond', 'enamored')
    hashmap1.add('wrath', 'anger')
    hashmap1.add('diligent', 'employed')
    hashmap1.add('outfit', 'garb')
    hashmap1.add('guide', 'usher')

    hashmap2.add('fond', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam')

    print(left_joiner(hashmap1, hashmap2))
