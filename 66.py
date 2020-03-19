from math import sqrt
from itertools import product
"""
plan of attack:
we generate the first 10000 square numbers
we loop over d<1000
    we multiply squares * d [dsquares]
    we [x for x,y in product(squares, dsquares) if x - y == 1]
    we sort that list, if the first element bigger than the max, max=that result

Hmmm, product(squares, dsquares) is too slow. try double nested loop instead
IDeas:
- keep track of which numbers don't produce a result at all, look if it has a pattern. If so, filter out.
    |_ the pattern might be if d is n^2
"""
noresult = []
squares = [i*i for i in range(1,10000)] # change from list comperhension to generator expression
maxx = ((0,0),13)
for d in range(1,100):
    dsquares = [i * d for i in squares] # change from list comperhension to generator expression
    res = []
    for x in squares: # Break the x-squares loop if we have a result
        for y in dsquares: # break innermost loop if y > x or x-y = 1. 
            if x - y == 1:
                res = [(int(sqrt(x)), int(sqrt(y/d))), d]
                break
            elif y > x:
                break
        if res:
            break
    if res:
        if res[0][0] > maxx[0][0]:
            maxx = res
            print("new max x={},y={} for d={}".format(maxx[0][0],maxx[0][1], maxx[1]))
    else:
        noresult.append(d)



print("max x={} for d={}".format(maxx[0], maxx[1]))
print("no x or y found in", noresult )