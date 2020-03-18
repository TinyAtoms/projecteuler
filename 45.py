import numpy as np


start = 143
stop = 10000

n = np.arange(start, stop)
triangle = n*(n+1)/2
pentagon = n*(3*n-1)/2
hexagon = n*(2*n-1)

temp = [i for i in triangle if i in pentagon and i in hexagon]
print(temp)