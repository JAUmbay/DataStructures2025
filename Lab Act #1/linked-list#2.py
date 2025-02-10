class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def demonstrate_linked_list():
    linked_list = LinkedList()
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(15)
    linked_list.display()
    linked_list.delete(10)
    linked_list.display()

demonstrate_linked_list()
