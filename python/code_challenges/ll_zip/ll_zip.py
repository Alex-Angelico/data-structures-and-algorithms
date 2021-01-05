from linked_list import Node, LinkedList
# code_challenges.linked_list


def zipLists(llist1, llist2):
    first_current = llist1.head
    print('FIRST_CURRENT: ', first_current.data)
    second_current = llist2.head
    print('SECOND_CURRENT: ', second_current.data)

    hold_next = []
    hold_next_next = []

    while first_current or second_current:
        # if hold_next == []:
        #     hold_next = first_current.next
        #     print('HOLD TEST IF: ', hold_next)
        #     # break
        # else:
        #     hold_next = hold_next_next
        #     print('HOLD TEST ELSE: ', hold_next.data)
        # print('THRESHOLD 0')
        if first_current.next.next:
            hold_next = first_current.next
            hold_next_next = first_current.next.next
            first_current.next = second_current
            # hold_next_next = first_current.next.next
            first_current.next.next = hold_next
            second_current = second_current.next
            first_current = first_current.next.next
        print(llist1)

    return llist1


llist_a, llist_b = LinkedList(), LinkedList()

llist_a.insert(23)
llist_a.insert(98)
llist_a.insert(415)
llist_a.insert(123)
llist_a.insert(981)
llist_a.insert(454)
llist_a.insert(213)

llist_b.insert(198)
llist_b.insert(455)
llist_b.insert(253)
llist_b.insert(978)
llist_b.insert(203)
llist_b.insert(918)
llist_b.insert(45)

x = zipLists(llist_a, llist_b)

print('test:', x)
