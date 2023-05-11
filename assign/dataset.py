from distutils.log import info
from itertools import count
import networkx as nx
import matplotlib.pyplot as plt

#Degree Distribution : How many Nodes are there in the network that have a possible degree
def plot_deg_dist(G):
   all_degrees = nx.degree(G)#To get all degrees
   unique_degrees = list(set(all_degrees))
   count_degrees = []
   for i in unique_degrees:
      x = all_degrees.count(i)
      count_degrees.append(x)
   plt.plot(unique_degrees,count_degrees,'yo-')
   plt.xlabel('Degrees in G')
   plt.ylabel('Number of Nodes')
   plt.title("Degree Distribtion of Football Network")
   plt.show()

# G = nx.read_edgelist('twitter_combined.txt')#Reads The Network Dataset and Give a graph
# To know the info we use info() method from Networkx with G as parameter 
G = nx.read_pajek('football.net')
'''print(nx.info(G))
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(nx.is_directed(G))
print(nx.info(H))
print(nx.number_of_nodes(H))
print(nx.number_of_edges(H))
print(nx.is_directed(H))'''
# To Visualize the graph we use following function
# To draw the graph
# nx.draw(G)
# To draw a circular layout
# nx.draw_circular(G)
# Different layouts are available in networkx
# nx.draw_spring(G)

#To Show the Graph
# plt.show()
# Power Law Distribution
plot_deg_dist(G)

