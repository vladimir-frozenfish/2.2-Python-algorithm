from node_list import print_linked_list


class DoubleConnectedNode:
    """класс двухсвязного списка"""
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def nodeDouble_list_reverse(node):
    """функция вовзращает голову перевернутого двусвязного списка"""
    while True:
        node.next, node.prev = node.prev, node.next
        if node.prev is None:
            return node
        node = node.prev


if __name__ == '__main__':
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    print_linked_list(node0)

    reverse_head = nodeDouble_list_reverse(node0)
    print_linked_list(reverse_head)


    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1