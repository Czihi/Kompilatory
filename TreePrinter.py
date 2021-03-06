from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.LinesOpt)
    def printTree(self, indent=0):
        if self.lines:
            self.lines.printTree()

    @addToClass(AST.Lines)
    def printTree(self, indent=0):
        for line in self.lines:
            line.printTree(indent)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        pass
        # fill in the body


    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body


    # define printTree for other classes
    # ...

