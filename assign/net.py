import networkx as nt
import matplotlib.pyplot as plt

# G = nt.Graph()

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)

# G.nodes()

# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(3,4)
# G.add_edge(1,4)
# G.add_edge(1,3)

# G.edges()

# nt.draw(G)
# plt.show()

H = nt.complete_graph(10)
print(H.nodes())
print(H.edges())
# No. of Nodes
print(H.order())
# No. of Edges
print(H.size())

# nt.draw(H,with_labels=1)
# plt.show()


G = nt.gnp_random_graph(20,0.5)
nt.draw(G,with_labels = 1)
plt.show()