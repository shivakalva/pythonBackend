from pythonBackend.Functions.konstructor import konstructor


class inherit(konstructor):
    numsa = 5

    def __init__(self):
        konstructor.__init__(self, 4, 5)

    def getcompletedata(self):
        return self.numsa + self.vars + self.summation()


child = inherit()
print(child.getcompletedata())
