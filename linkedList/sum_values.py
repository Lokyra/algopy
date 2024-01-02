class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    res = []
    current = head
    while current is not None:
        res.append(current.val)
        current = current.next

    return res


def linked_list_values_rec(head):
    values = []

    fill_values(head, values)

    return values


def fill_values(head, values):
    if head is None:
        return

    values.append(head.val)
    fill_values(head.next, values)
