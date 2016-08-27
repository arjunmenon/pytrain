#
# test Feedforward Neural Network
#
# @ author becxer
# @ e-mail becxer87@gmail.com
# 

from test_pytrain import test_Suite
from pytrain.NeuralNetwork import FNN
from pytrain.lib import batch
from numpy import *

class test_FNN(test_Suite):

    def __init__(self, logging = True):
        test_Suite.__init__(self, logging)

    def test_process(self):

        train_mat = [\
                     [0.12, 0.25],\
                     [3.24, 4.33],\
                     [0.14, 0.45],\
                     [7.30, 4.23],\
                     ]
        train_label = ['zero','one','zero','one']
        
        fn = FNN(train_mat, train_label, [3,2])
        fn.fit(0.1, 5000, 0.001)
        r1 = batch.eval_predict_one(fn, [4.40,4.37], 'one', self.logging)
        r2 = batch.eval_predict_one(fn, [0.40,0.37], 'zero', self.logging)
        
