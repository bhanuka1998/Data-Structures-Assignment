class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def remove(self, data):
        if self.head:
            current_node = self.head
            if self.head == self.tail:
                if current_node.data == data:
                    self.head = None
                    self.tail = None
                return
            else:
                if current_node.data == data:
                    self.head = current_node.next_node
                    return
                prev_node = current_node
                current_node = current_node.next_node
                while current_node.next_node:
                    if current_node.data == data:
                        prev_node.next_node = current_node.next_node
                        return
                    prev_node = current_node
                    current_node = current_node.next_node

                if current_node.data == data:
                    prev_node.next_node = None
                    self.tail = prev_node

    def __contains__(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next_node

        return False

# ll = LinkedList()
# ll.append(1)
# ll.append(5)
# ll.append(3)
# ll.append(9)
# ll.append(7)

# for i in range(10):
#     print(f'Is {i} in ll: {i in ll}')


# ### To use with Clean Park, follow the code below. No further changes should be necessary.

# from linked_list import LinkedList


# class Clean_park:
#     def __init__(self):
#         self.customer_list = []
#         self.customer_id_list = LinkedList