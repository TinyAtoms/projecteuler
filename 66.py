from itertools import product
from math import sqrt
import numpy as np
from tools.itertools import cartesian


squares = [i*i for i in range(1,10000)]
maxx = ((649,0),13)
for d in range(12,50):
    dsquares = [i * d for i in squares]
    res = []
    for x in squares:
        for y in dsquares:
            if x - y == 1:
                res = [(int(sqrt(x)), int(sqrt(y/d))), d]
                break
            if x - y < 1:
                break
        if res:
            break
    if res:
        if res[0][0] > maxx[0][0]:
            maxx = res
            print("new max x={} for d={}".format(maxx[0][0], maxx[1]))



print("max x={} for d={}".format(maxx[0], maxx[1]))
