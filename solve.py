import os
import sys

import numpy as np

import caffe

import score

try:
    import setproctitle
    setproctitle.setproctitle(os.path.basename(os.getcwd()))
except:
    pass

weights = './model/voc_fcn32s_trans_init.caffemodel'

# init
caffe.set_device(0)
caffe.set_mode_gpu()

solver = caffe.SGDSolver('./model/solver.prototxt')
solver.net.copy_from(weights)

# scoring
val = np.loadtxt('./data/segvalid11.txt', dtype=str)

for _ in range(25):
    solver.step(8498)
    ##score.seg_tests(solver, False, val, layer='score')
    score.seg_tests(solver, 'val_score_{0}', val, layer='score')
