import matplotlib.pyplot as plt
import networkx as nx

import social_graph

if __name__ == '__main__':
    fig = plt.figure(figsize=(24, 24))
    target = "fegor2004"
    cnt = 1
    graph_nx = social_graph.get_friends_nx_graph(target, cnt)
    nx.write_adjlist(graph_nx, f"{target}_friends_graph_{cnt}_1.adjlist")
