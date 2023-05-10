# Model road network of cities in Nrt
 
import networkx as nx
import random
import matplotlib.pyplot as plt


# Undirected Graph
G = nx.Graph() 

# G = nx.DiGraph() Directed Graph 

nr = [x for x in input().split() ]

for area in nr :
    G.add_node(area)

cost = []
value = 100
for val in range(0,2001,100):
    cost.append(val)
n = G.order()

for i in range((n*(n-1))//2):
    c1 = random.choice(list(G.nodes()))
    c2 = random.choice(list(G.nodes()))
    if (c1!=c2) and (G.has_edge(c1,c2)) == 0:
        w = random.choice(cost)
        G.add_edge(c1, c2, weight=w)
'''
#For spectral layout
# "pos = nx.spectral_layout(G)"
#For Circular Layout
# pos = nx.circular_layout(G)
# nx.draw(G,pos,with_labels=1)
# For labelling Edge weights
# nx.draw_networkx_edge_labels(G, pos)
# plt.show()'''


'''# To Check If there is a path between nodes
for u in G.nodes():
    for v in G.nodes():
        print(u,v,nx.has_path(G,u,v))


# To Check If graph is connected or not
print(nx.is_connected(G))'''

