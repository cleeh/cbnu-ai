from treelib import Node, Tree

class Perceptron:
    def __init__(self, W, w0 = 0):
        if W.ndim > 1:
            raise Exception('The size of W dimension must be 1') 
        self.W = W
        self.w0 = w0
    
    def predict(self, X):
        if X.ndim > 1:
            raise Exception('The size of X dimension must be 1')
        elif X.shape[0] != self.W.shape[0]:
            raise Exception('X and W must be the same length')
        return (self.W * X).sum() + self.w0
    
    def show(self):
        tree = Tree()
        tree.create_node('w0({})'.format(self.w0), 'bias')
        for i in range(self.W.shape[0]):
            tree.create_node('W{}({})'.format(i + 1, self.W[i]), i, 'bias', i)
        tree.show()
        