import networkx as nx
import matplotlib.pyplot as plt

# nx.test()
G = nx.MultiDiGraph()
# G.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
# print(dict(G.degree(weight='weight')))
H = nx.path_graph(10)
# MG.add_nodes_from(H)
G.add_edges_from([(83939, 38224), (83939, 83850), (38224, 3017)])
plt.subplot(111)
nx.draw(G, pos=nx.spring_layout(G), with_labels=True, edge_color='b', node_color='y')
plt.show()
# plt.savefig('call_graph.png')