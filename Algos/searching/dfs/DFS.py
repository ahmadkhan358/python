from Stack import Stack
from BSTree import BSTree

class DFS:
    def __init__(self):
        super().__init__()
        self.s = Stack()

    def inAction(self, tree):
        self.s.push(tree)
        d = []
        while True:
            container = self.s.pop()
            d.append(container.data)

            if container.right != None:
                self.s.push(container.right)

            if container.left != None:
                self.s.push(container.left)


            if self.s.isEmpty() == True:
                break
        return d

            
if __name__ == "__main__":
    tree = BSTree()
    tree.insert(162)
    tree.insert(16)
    tree.insert(45)
    tree.insert(8)
    tree.insert(99)
    x = tree.insert(67)
    
    dfs = DFS()
    l = dfs.inAction(x)

    print(l)