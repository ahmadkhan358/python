class Stack():

    def __init__(self):
        self.top = -1
        self.values = []

    def push(self, value):
        self.values.append(value)
        self.top += 1

    def pop(self):
        if self.top < 0:
            return "Nothing to pop"

        self.top -= 1
        return self.values.pop()

    def whereIstop(self):
        return self.top


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())