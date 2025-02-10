class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def is_empty(self): return not self.items

def reverse_string(s):
    stack = Stack()
    for char in s: stack.push(char)
    return ''.join([stack.pop() for _ in s])

def evaluate_postfix(expr):
    stack = Stack()
    for token in expr.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.push(eval(f'{a} {token} {b}'))
    return stack.pop()

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None
    def front(self): return self.items[0] if self.items else None

def people_in_line():
    queue = Queue()
    for person in ["Alice", "Bob", "Charlie"]:
        queue.enqueue(person)
    print(queue.dequeue(), queue.dequeue(), "Next:", queue.front())

def customer_service():
    queue = Queue()
    for customer in ["Customer 1", "Customer 2", "Customer 3"]:
        queue.enqueue(customer)
    print(queue.dequeue(), queue.dequeue(), "Next:", queue.front())

def array_operations():
    arr = [10, 20, 30, 40, 50]
    print("First:", arr[0], "Last:", arr[-1])
    print("Elements:", *arr)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if not self.head: self.head = node
        else: self._get_last().next = node
    
    def _get_last(self):
        node = self.head
        while node.next: node = node.next
        return node

    def display(self):
        node = self.head
        while node: 
            print(node.data, end=" -> ")
            node = node.next
        print("None")

    def delete(self, data):
        node = self.head
        if node and node.data == data: self.head = node.next
        else:
            prev = None
            while node and node.data != data:
                prev, node = node, node.next
            if node: prev.next = node.next

def linked_list_example():
    ll = LinkedList()
    for val in [10, 20, 30]: ll.append(val)
    ll.display()
    ll.delete(20)
    ll.display()

if __name__ == "__main__":
    print("Reverse String:", reverse_string("hello"))
    print("Postfix Evaluation:", evaluate_postfix("3 4 + 2 * 7 /"))
    
    print("\nPeople in Line:")
    people_in_line()
    print("Customer Service:")
    customer_service()
    
    print("\nArray Operations:")
    array_operations()
    
    print("\nLinked List Example:")
    linked_list_example()
