from linked_list import *
import random


def linker(l1, l2):
    dummy_head = tail = ListNode()
    while not l1.data or not l2.data:
        l1 = l1 if l1.data else l1.next
        l2 = l2 if l2.data else l2.next
    while l1 and l2:
        if l1.data > l2.data:
            tail.next, l2 = l2, l2.next
        else:
            tail.next, l1 = l1, l1.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy_head.next


if __name__ == "__main__":
    list_1 = ListNode()
    list_2 = ListNode()
    rand = random.randint(0, 50)
    for i in reversed(range(rand)):
        new_node = ListNode(i)
        if i % 2 == 0:
            list_1.insert_after(new_node)
        else:
            list_2.insert_after(new_node)

    dummy_list = linker(list_1, list_2)
    while dummy_list:
        print(dummy_list.data, end=' ')
        dummy_list = dummy_list.next
    # test for unique sorted lists
    # dummy_list_1 = ListNode(0)
    # dummy_list_2 = ListNode(0)
    # dummy_list_1 = list_1.next
    # dummy_list_2 = list_2.next
    # while dummy_list_1 and dummy_list_2:
    #     print(dummy_list_1.data, end=' ')
    #     print(dummy_list_2.data, end=' ')
    #     dummy_list_1 = dummy_list_1.next
    #     dummy_list_2 = dummy_list_2.next
