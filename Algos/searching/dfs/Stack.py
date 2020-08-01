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

    def isEmpty(self):
        if self.top == -1:
            return True
        
        return False


