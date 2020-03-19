from tools.collections import mil_primes
import networkx as nx
import matplotlib.pyplot as plt

def hamming_distance(a,b):
    a = str(a)
    b = str(b)
    if len(a) - len(b):
        raise IndexError("Size of a and b don't match")
    count = 0
    for i, letter in enumerate(a):
        if letter != b[i]:
            count +=1
    return count

def modified_hamming(a,b):
    a = str(a)
    b = str(b)
    if len(a) - len(b):
        raise IndexError("Size of a and b don't match")
    count = 0
    letters = []
    for i, letter in enumerate(a):
        if letter != b[i]:
            count +=1
            letters.append(b[i])
    if len(set(letters)) == 1:
        return count
    return None


hundreds = mil_primes[mil_primes<1000]
hundreds = hundreds[hundreds > 99]

graph = nx.Graph()
for i in hundreds:
    for j in hundreds:
        distance = modified_hamming(i,j)
        if distance:
            graph.add_edge(i,j, weight=distance)

# nx.draw(graph)
# plt.show()
for i in hundreds:
    print(graph[i])
    break