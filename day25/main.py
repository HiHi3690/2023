import re
import networkx as nx
import math

input = [[y.split() for y in x.split(": ")] for x in open("data.txt").read().split("\n")]

G = nx.Graph()

for s,el in input:
    G.add_edges_from([(s[0],e) for e in el])

bridges = nx.minimum_edge_cut(G)
G.remove_edges_from(bridges)

groups = nx.connected_components(G)
result = math.prod([len(g) for g in groups])

print(result) #520380