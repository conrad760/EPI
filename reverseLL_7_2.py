from linked_list import *
import random


def reverseLL(L, start, finish):
    dummy_head = sub = ListNode(1, L)
    for _ in range(1, start):
        sub = sub.next
    sub_iter = sub.next
    for _ in range(finish - start):
        temp = sub_iter.next
        sub_iter.next, temp.next, sub.next = (temp.next, sub.next, temp)

    return dummy_head.next


if __name__ == "__main__":
    rand = random.randint(9, 10)
    list = ListNode(0)
    list.make_ll(rand)
    start = random.randint(0, rand) # start = 2
    finish = random.randint(start, rand) # finish = 5
    list.print_ll()
    fin = reverseLL(list, start, finish)
    print()
    fin.print_ll()
