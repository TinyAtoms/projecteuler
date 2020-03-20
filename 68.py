from itertools import combinations, chain
from collections import defaultdict, Counter
import networkx as nx
from matplotlib import pyplot as plt

def generate_solutionset(n):

    nums = [i for i in range(1,2 * n + 1)]

    solution = defaultdict(list)

    for c in combinations(nums, 3):
        csum = sum(c)
        cstring = [i for i in c][::-1]
        solution[csum].append(cstring)
    popped = []
    for k,v in solution.items():
        if len(v) < n:
            popped.append(k)
    for k in popped:
        solution.pop(k)
    return solution





def gen_graph(nodeset, n=3):
    nums = [i for i in range(1,2 * n + 1)]
    nodecounts = Counter(chain.from_iterable(nodeset))
    inner = [k for k,v in nodecounts.items() if v == 2]
    outer = [i for i in nums if i not in inner]
    print(outer, inner)
    print(nodeset)

    

nodeset = generate_solutionset(3)
gen_graph(nodeset[9])