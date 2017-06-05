'''
Create color map for PASCAL VOC dataset.
'''

import numpy as np


# Get the specified bit value
def _bitget(byteval, idx):
  return ((byteval & (1 << idx)) != 0)

# Create label-color map, label --- [R G B]
#  0 --- [  0   0   0],  1 --- [128   0   0],  2 --- [  0 128   0]
#  4 --- [128 128   0],  5 --- [  0   0 128],  6 --- [128   0 128]
#  7 --- [  0 128 128],  8 --- [128 128 128],  9 --- [ 64   0   0]
# 10 --- [192   0   0], 11 --- [ 64 128   0], 12 --- [192 128   0]
# 13 --- [ 64   0 128], 14 --- [192   0 128], 15 --- [ 64 128 128]
# 16 --- [192 128 128], 17 --- [  0  64   0], 18 --- [128  64   0]
# 19 --- [  0 192   0], 20 --- [128 192   0], 21 --- [  0  64 128]
def labelcolormap(N=256):
  color_map = np.zeros((N, 3))
  
  for n in xrange(N):
    id_num = n
    r, g, b = 0, 0, 0
    
    for pos in xrange(8):
      r = np.bitwise_or(r, (_bitget(id_num, 0) << (7-pos)))
      g = np.bitwise_or(g, (_bitget(id_num, 1) << (7-pos)))
      b = np.bitwise_or(b, (_bitget(id_num, 2) << (7-pos)))
      id_num = (id_num >> 3)
    color_map[n, 0] = r
    color_map[n, 1] = g
    color_map[n, 2] = b
  
  return color_map
