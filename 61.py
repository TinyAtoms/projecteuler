import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


'''
plan of attack:
generate all numbers between 1000 and 10000, 
then make a directional graph where
1234 is a predecessor of 3456 and 5678 is a successor of 3456
then keep deleting nodes that don't have a predecessor or successor
in the end, we should end up with a cyclical graph, hopefully
then plot the graph or print the nodes, idk
Welp, this is a bust.
because you can get cycles from tri>square>tri>square for example, and this will contain cycles
an idea is to name nodes number_(numbertype)
and then to eliminate cycles with multiple numbertypes
that was somewhat helpful
but only like so:
making it a graph and addint numbertype allowed me to filter out unnneeded nodes
i then bruteforced it
the difference between straight bruteforce and not is a 66% increase in speed
'''

def gen_triangle(n):
    return int((n * n + n)/2)

def gen_square(n):
    return n * n

def gen_pent(n):
    return int((3 * n * n - n )/2 )

def gen_hex(n):
    return 2 * n * n - n

def gen_hepta(n):
    return int((5*n * n - 3 * n)/2)

def gen_octa(n):
    return 3 * n * n - 2 * n




triangles = []
squares = []
pentas = []
hexas = []
heptas = []
octas = []
for i in range(1,150):
    triangles.append(gen_triangle(i))
    squares.append(gen_square(i))
    pentas.append(gen_pent(i))
    hexas.append(gen_hex(i))
    heptas.append(gen_hepta(i))
    octas.append(gen_octa(i))

triangles = np.array(triangles)
triangles = triangles[triangles < 10000]
triangles = triangles[triangles > 999]
triangles = triangles.astype(np.str)
squares = np.array(squares)
squares = squares[squares < 10000]
squares = squares[squares > 999]
squares = squares.astype(np.str)
pentas = np.array(pentas)
pentas = pentas[pentas < 10000]
pentas = pentas[pentas > 999]
pentas = pentas.astype(np.str)
hexas = np.array(hexas)
hexas = hexas[hexas < 10000]
hexas = hexas[hexas > 999]
hexas = hexas.astype(np.str)
heptas = np.array(heptas)
heptas = heptas[heptas < 10000]
heptas = heptas[heptas > 999]
heptas = heptas.astype(np.str)
octas = np.array(octas)
octas = octas[octas < 10000]
octas = octas[octas > 999]
octas = octas.astype(np.str)

graph = nx.DiGraph()



for i in triangles:
    graph.add_edges_from([((i+"tri", x+"squ") ) for x in squares if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([((x+"squ", i+"tri") ) for x in squares if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([((i+"tri", x+"pen") ) for x in pentas if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([((x+"pen", i+"tri") ) for x in pentas if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([((i+"tri", x+"hex") ) for x in hexas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([((x+"hex", i+"tri") ) for x in hexas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([((i+"tri", x+"hep") ) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([((x+"hep", i+"tri") ) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([((i+"tri", x+"oct") ) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([((x+"oct", i+"tri") ) for x in octas if x[2:] == i[:2]]) # back_octas

for i in squares:
    graph.add_edges_from([((i+"squ", x+"pen") ) for x in pentas if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([((x+"pen", i+"squ") ) for x in pentas if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([((i+"squ", x+"hex") ) for x in hexas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([((x+"hex", i+"squ") ) for x in hexas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([((i+"squ", x+"hep") ) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([((x+"hep", i+"squ") ) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([((i+"squ", x+"oct") ) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([((x+"oct", i+"squ") ) for x in octas if x[2:] == i[:2]]) # back_octas

for i in pentas:
    graph.add_edges_from([((i+"pen", x+"hex") ) for x in hexas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([((x+"hex", i+"pen") ) for x in hexas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([((i+"pen", x+"hep") ) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([((x+"hep", i+"pen") ) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([((i+"pen", x+"oct") ) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([((x+"oct", i+"pen") ) for x in octas if x[2:] == i[:2]]) # back_octas

for i in hexas:
    graph.add_edges_from([((i+"hex", x+"hep") ) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([((x+"hep", i+"hex") ) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([((i+"hex", x+"oct") ) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([((x+"oct", i+"hex") ) for x in octas if x[2:] == i[:2]]) # back_octas

for i in heptas:
    graph.add_edges_from([(i+"hep", x+"oct") for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x+"oct", i+"hep") for x in octas if x[2:] == i[:2]]) # back_octas


old = len(graph.nodes())
while len(graph.nodes()) > 6:
    remove_nodes = []
    for node in graph.nodes():
        if not list(graph.successors(node)) or not list(graph.predecessors(node)):
            remove_nodes.append(node)
    for n in remove_nodes:
        graph.remove_node(n)
    if not remove_nodes:
        break
print(old, "reduced to", len(list(graph.nodes())), "nodes")

numbers = {
    "tri" : [],
    "squ" : [],
    "pen" : [],
    "hex" : [],
    "hep" : [],
    "oct" : []
}
for node in graph.nodes():
    numbers[node[-3:]].append(node[:-3])

# numbers = {
#     "tri" : triangles,
#     "squ" : squares,
#     "pen" : pentas,
#     "hex" : hexas,
#     "hep" : heptas,
#     "oct" : octas
# }




from itertools import combinations, permutations

names = ["tri", "squ", "pen", "hex", "hep", "oct"]
for i in permutations(names, 6):
    for tri in numbers[i[0]]:
        for squ in numbers[i[1]]:
            if tri[2:] != squ[:2]:
                continue
            for pen in numbers[i[2]]:
                if squ[2:] != pen[:2]:
                    continue
                for he in numbers[i[3]]:
                    if pen[2:] != he[:2]:
                        continue
                    for hep in numbers[i[4]]:
                        if he[2:] != hep[:2]:
                            continue
                        for oc in numbers[i[5]]:
                            if hep[2:] != oc[:2]:
                                continue
                            if tri[:2] != oc[2:]:
                                continue
                            res = [tri, squ, pen, he, hep, oc]
                            print(res, sum([int(i) for i in res]))
