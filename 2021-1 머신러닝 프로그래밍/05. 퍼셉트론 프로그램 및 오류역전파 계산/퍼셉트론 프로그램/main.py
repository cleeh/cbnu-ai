import random
import numpy as np
from perceptron import Perceptron

PERCEPTRON_SIZE = 9
BIAS_DEVIATION = 5
if __name__ == '__main__':
    W = np.random.rand(PERCEPTRON_SIZE)
    X = np.random.rand(PERCEPTRON_SIZE)
    w0 = random.randrange(-BIAS_DEVIATION, BIAS_DEVIATION+1)
    perceptron = Perceptron(W, w0)
    perceptron.show()

    print('W: {}'.format(W))
    print('X: {}'.format(X))
    print('w0: {}'.format(w0))
    print(perceptron.predict(X))
    