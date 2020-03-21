import csv
import networkx as nx

'''
graph traversal is a bust
'''

def gen_edges_triangle(triangle):
    '''
    generates edges for a triangular directional graph.
    input: 
    [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]
    output: [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (3, 6), (4, 7), (4, 8), (5, 8), (5, 9), (6, 9), (6, 10)]
    '''
    edges = []
    # 1-2, 1-3, 2-4, 2-5, 3-5, 3-6, etd
    for i, row in enumerate(graph[:-1]):
        for j, cell in enumerate(row):
            preds = [triangle[i +1][j] +"_{}_{}".format(i+1,j), triangle[i+1][j+1]+"_{}_{}".format(i+1,j+1)]
            preds = [(a, cell+"_{}_{}".format(i,j)) for a in preds]
            edges += preds
    return edges

with open("67.csv", "r") as problemfile:
    problem = csv.reader(problemfile)
    graph = [[int(a) for a in i] for i in problem]

# edges = gen_edges_triangle(graph)
# source = edges[0][0]
# destinations =list(set([i[1] for i in edges[-198:]])) 
# triangle = nx.DiGraph()
# triangle.add_edges_from(edges)
# paths = []
# for d in destinations[::-1]:
#     temp = nx.algorithms.shortest_paths.all_shortest_paths(triangle,d,  source, weight=1, method="bellman-ford")
#     print(list(temp))
#     break

# print(graph)
# graph = [
#     [1],
#     [2,3],
#     [4,5,6],
# ]
graph = list(reversed(graph))

for i, row in enumerate(graph[:-1]):
    for j, cell in enumerate(row[:-1]):
        temp_max = max(cell, graph[i][j+1])
        graph[i+1][j] += temp_max
print(graph)


