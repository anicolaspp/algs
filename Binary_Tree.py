class BinaryNode:
    def __init__(self, value = 0, Rigth = None, Left = None):
        self.Value = value
        self.Left = Left
        self.Rigth = Rigth
        self.EsHoja = 1

    def Contains(self, value):
        if self.Value == value:
            return 1
        else:
            if self.Value < value:
                if self.Rigth != None:
                    return self.Rigth.Contains(value)
                else:
                    return 0
            else:
                if self.Left != None:
                    return self.Left.Contains(value)
                else:
                    return 0


    def Add(self, value):
        if self.Value == value:
            return 0
        else:
            if self.Value < value:
                if self.Rigth == None:
                    self.Rigth = BinaryNode(value)
                    return 1
                else:
                    return self.Rigth.Add(value)
            else:
                if self.Left == None:
                    self.Left = BinaryNode(value)
                    return 1
                else:
                    return self.Left.Add(value)

    def __InOrden__(self):
        if self.Left != None:
           for i in self.Left.__InOrden__():
               yield i
        yield self.Value
        if self.Rigth != None:
           for i in self.Rigth.__InOrden__():
               yield i

class BinaryTree:
    def __init__(self, value):
        self.Root = BinaryNode(value)

    def Add(self, value):
        return self.Root.Add(value)

    def InOrden(self):
        return self.Root.__InOrden__()

    def Contains(self, value):
        return self.Contains(value)

def Add(x):
    x.Add(10)
    x.Add(7)
    x.Add(9)
    x.Add(1)
    x.Add(4)
    x.Add(3)

def Print_Tree(x):
    for i in x.InOrden():
        print i



