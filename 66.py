from math import sqrt
import numpy as np
"""
plan of attack:
1.
we generate the first 10000 square numbers
we loop over d<1000
    we multiply squares * d [dsquares]
    we [x for x,y in product(squares, dsquares) if x - y == 1]
    we sort that list, if the first element bigger than the max, max=that result
2.
so i went with a numpy implementation.
i could then do
for d in somerange:
    dsquares = squares * d
    for x in squares:
        tempy = dsquares [dsquares < x]
        y = tempy[-1]
        do checking stuff
cuts down a bit of the time
3.
I created a function that generates x,y pairs, and keeps generating the next one untill y is an integer
then i test it if it works, if not, i continue generating the next highest number.
problems with it:
the numbers which don't produce a result

The abovementoned methods are all trash.

IDeas:
- keep track of which numbers don't produce a result at all, look if it has a pattern. If so, filter out.
    |_ the pattern might be if d is n^2
    |- 61 also has an unusually large unfindable x
    |- oh wow, i was just reading the problem statement, and if d = n^2, there is indeed no solution
- Go look at pell's equation and Lagrange-Mollin-Matthews method
    |- this definitely isn't a problem solved with bruteforce, seeing as the answer for 61 > 1000000000
    |- the math looks a whole lot of nonfun
    |- wikipedia told me the answer was 1069

"""
# def gen_xy(d, last, limit=10000000000):
#     while last < limit:
#         x = last + 1
#         dy = (x * x - 1)/d
#         y = sqrt(dy)
#         last = x
#         if int(y) == y:
#             break
#         if last >= limit:
#             last = None
#             break
#     return x,dy, last

# result = [97,62809633] # d, x
# squares = set([i * i for i in range(1,32)])
# for d in range(result[0],1001):
#     if d in squares:
#         continue
#     res = [0,0]
#     last = 1
#     while True:
#         x, dy, last = gen_xy(d, last)

#         if x* x - d * dy ==1:
#             res = [d, x]
#             break
#         if not last:
#             print("LIMIT REACHED, SANITY CHECK at", d)
#             res = [0,0]
#             break
#     if res[1] > result[1]:
#         result = res
#         print("new max x={} at d={}".format(res[1], res[0]))



# def lmm_method(d, n=1):
#     om = sqrt(5)/1
#     for i in range(d):

