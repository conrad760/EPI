class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def search_list(L, key):
        while L and L.data != key:
            L = L.next
        return L

    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node

    def delete_next(node):
        node.next = node.next.next

    def make_ll(self, num):
        for i in reversed(range(1, num)):
            new_node = ListNode(i)
            self.insert_after(new_node)
        return self

    def print_ll(self):
        while self:
            print(self.data, end=" ")
            self = self.next
