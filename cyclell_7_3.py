from linked_list import *


def loop_check(head):
    def len_cyc(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle = head
            for _ in range(len_cyc(slow)):
                cycle = cycle.next
            it = head
            while it is not cycle:
                it = it.next
                cycle = cycle.next
            return it
    return None


if __name__ == "__main__":

    list = ListNode()
    list.make_ll(10)
    list.next.next.next.next.next.next = list.next.next.next
    fin = loop_check(list)
    for _ in range(100):
        print(fin.data, end=" ")
        fin = fin.next
