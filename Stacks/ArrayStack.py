class ArrayStack:
    """LIFO Stack Implementation using a Python list as underlying storage"""
    
    def __init__(self):
        """Create an empty stack"""
        self._data = []  #non public List Instance

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is Empty"""
        return len(self._data) == 0

    def push(self,e):
        """Add element e to the top of the stack"""
        self._data.append(e)  #new item is stored at the end of the list

    def top(self):
        """Return (but do not remove) the top most element in the stack"""
        """Raise Empty Exception if the stack is empty"""

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        """Remove and return the top most element in the stack"""
        """Raise Empty Exception if the stack is empty"""
        if is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() #remove the last element from list

stack = ArrayStack()
print(stack.is_empty())
stack.push(8)
stack.push(9)
stack.push(10)
print(len(stack))   