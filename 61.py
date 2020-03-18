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
# print(triangles, squares, pentas, hexas, heptas, octas, sep="\n\n")
'''

squares end in 0,1,4,5,6,9
octas end in 0,1,3,5,6,8
what if you made a directional graph and then tried to display it to find the longest chain?
'''

graph = nx.DiGraph()
for i in triangles:
    graph.add_edges_from([(i, x) for x in squares if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([(x, i) for x in squares if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([(i, x) for x in pentas if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([(x, i) for x in pentas if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([(i, x) for x in hexas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([(x, i) for x in hexas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([(i, x) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([(x, i) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([(i, x) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x, i) for x in octas if x[2:] == i[:2]]) # back_octas

for i in squares:
    graph.add_edges_from([(i, x) for x in triangles if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([(x, i) for x in triangles if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([(i, x) for x in pentas if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([(x, i) for x in pentas if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([(i, x) for x in hexas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([(x, i) for x in hexas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([(i, x) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([(x, i) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([(i, x) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x, i) for x in octas if x[2:] == i[:2]]) # back_octas

for i in pentas:
    graph.add_edges_from([(i, x) for x in triangles if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([(x, i) for x in triangles if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([(i, x) for x in squares if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([(x, i) for x in squares if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([(i, x) for x in hexas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([(x, i) for x in hexas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([(i, x) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([(x, i) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([(i, x) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x, i) for x in octas if x[2:] == i[:2]]) # back_octas

for i in hexas:
    graph.add_edges_from([(i, x) for x in triangles if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([(x, i) for x in triangles if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([(i, x) for x in squares if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([(x, i) for x in squares if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([(i, x) for x in pentas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([(x, i) for x in pentas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([(i, x) for x in heptas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([(x, i) for x in heptas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([(i, x) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x, i) for x in octas if x[2:] == i[:2]]) # back_octas

for i in heptas:
    graph.add_edges_from([(i, x) for x in triangles if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([(x, i) for x in triangles if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([(i, x) for x in squares if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([(x, i) for x in squares if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([(i, x) for x in pentas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([(x, i) for x in pentas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([(i, x) for x in hexas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([(x, i) for x in hexas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([(i, x) for x in octas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x, i) for x in octas if x[2:] == i[:2]]) # back_octas

for i in octas:
    graph.add_edges_from([(i, x) for x in triangles if x[:2] == i[2:]]) # front_squares
    graph.add_edges_from([(x, i) for x in triangles if x[2:] == i[:2]]) # back_squares
    graph.add_edges_from([(i, x) for x in squares if x[:2] == i[2:]]) # front_pentas
    graph.add_edges_from([(x, i) for x in squares if x[2:] == i[:2]]) # back_pentas
    graph.add_edges_from([(i, x) for x in pentas if x[:2] == i[2:]]) # front_hexas
    graph.add_edges_from([(x, i) for x in pentas if x[2:] == i[:2]]) # back_hexas
    graph.add_edges_from([(i, x) for x in hexas if x[:2] == i[2:]]) # front_heptas
    graph.add_edges_from([(x, i) for x in hexas if x[2:] == i[:2]]) # back_heptas
    graph.add_edges_from([(i, x) for x in heptas if x[:2] == i[2:]]) # front_octas
    graph.add_edges_from([(x, i) for x in heptas if x[2:] == i[:2]]) # back_octas


while len(graph.nodes()) > 6:
    remove_nodes = []
    for node in graph.nodes():
        if not list(graph.successors(node)) or not list(graph.predecessors(node)) or graph.degree(node) < 2:
            remove_nodes.append(node)
    for n in remove_nodes:
        graph.remove_node(n)
    if not remove_nodes:
        break
print(len(list(graph.nodes())))

# pos=nx.spring_layout(graph)

cycles = nx.simple_cycles(graph)
for i in cycles:
    print(i)

# plt.subplot(121)
# nx.draw(graph, with_labels=True)
# plt.subplot(122)
# # nx.draw_shell(graph, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()
# G = nx.nx_agraph.to_agraph(graph)
# G.write("miles.dot")
# G.draw("miles.png",prog='neato')