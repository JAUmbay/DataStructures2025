class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop!")
            return None
        else:
            item = self.items.pop()
            print(f"Popped {item} from the stack.")
            return item

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty, cannot peek!")
            return None

    def is_empty(self):
        return len(self.items) == 0

def demonstrate_stack():
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print(f"Top item is: {stack.peek()}")
    stack.pop()
    print(f"Is stack empty? {stack.is_empty()}")

demonstrate_stack()
