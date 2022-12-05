class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True
    def operator(self):
        return self.data
    def left(self):
        return self.left
    def parent(self):
        return self.parent
    def isRoot(self):
        return self.parent is None
    def isExternal(self):
        return self.left is None and self.right is None
class BinaryTree:
    def __init__(self):
        self.root = Node(0,None)
    def add(self, data):
        if self.root.left is None and data%2 != 0:
            self.root.left = Node(data,self.root)
        elif self.root.right is None and data%2 == 0:
            self.root.right = Node(data,self.root)
        else:
            if data%2 != 0:
                self.root.left.insert(data)
            else:
                self.root.right.insert(data)
    def sumGanjil(self,node,ganjil=[]):
        if node is not None:
            self.sumGanjil(node.left,ganjil)
            ganjil.append(node.operator())
            self.sumGanjil(node.right,ganjil)         
        return ganjil

    def hasilGanjil(self):
        simpan = self.sumGanjil(self.root,ganjil=[])
        total = 0
        for isi in simpan:
            if isi%2 != 0:
                total += isi
        return "Penjumlahan data ganjil = "+str(total)

if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print(binaryT.hasilGanjil())
