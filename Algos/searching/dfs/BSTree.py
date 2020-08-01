from Node import Node
import random

class BSTree:
    def __init__(self):
        super().__init__()
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if self.root == None:
            self.root = newNode
        else:
            container = self.root
            while True:
                if container.data > newNode.data:
                    if container.left == None:
                        container.left = newNode
                        break
                    container = container.left
                elif container.data < newNode.data:
                    if container.right == None:
                        container.right = newNode
                        break
                    container = container.right
                else:
                    print("No duplicate values")
                    break

        return self.root

    def search(self, val):
        container = self.root

        while container != None:
            if val == container.data:
                return "Found"
            elif val < container.data:
                container = container.left
            else:
                container = container.right

        return "Not Found"


    def makeRandomTree(self):
        s = set()
        for i in range(10):
            s.add(random.randrange(5, 50))

        for i in s:
            self.insert(i)

        return self.root

