from node_list import Node, print_linked_list


def get_node_by_index(node, index):
    """функция возвращает элемент в связном списке указанного индекса"""
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head, index, value):
    """функция вставки элемента в связный список по индексу"""
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


def delete_node(head, index):
    """функция удалает элемент из связного списка по индексу, возвращает голову списка"""
    if index == 0:
        return head.next
    previous_node = get_node_by_index(head, index - 1)
    previous_node.next = previous_node.next.next
    return head


def search_node(head, value):
    """функция возвращает индекс элемента в связном с списке а заданным значением - value"""
    count = 0
    while head:
        if head.value == value:
            return count
        count += 1
        head = head.next
    return None


if __name__ == '__main__':
    n3 = Node('third')
    n2 = Node('second', n3)
    n1 = Node('first', n2)
    print_linked_list(n1)

    n0 = Node('zero', n1)
    print_linked_list(n0)

    n_minus = insert_node(n0, 0, 'minus')
    print_linked_list(n_minus)

    n2_5 = insert_node(n_minus, 4, 'two_and_half')
    print_linked_list(n_minus)

    delete_node(n_minus, 4)
    print_linked_list(n_minus)

    new_head = delete_node(n_minus, 0)
    print_linked_list(new_head)

    print(search_node(new_head, 'first'))