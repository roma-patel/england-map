import requests
import re
import os
import math
import json
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import networkx as nx
import collections
import operator

def check_visualisation():
    kwargs = {'arrowsize': 20, 'width': 2.5, 'node_size': 30}
    boundary_coords = [(0, 0), (2, 2), (3, 3), (3, 5), (5, 5), (7, 5),
            (8, 4), (9, 3), (7, 2), (5, 2), (3, 1)]
    G = nx.Graph()

    for coord in boundary_coords:
        G.add_node(len(G), pos=[coord[0], coord[1]])

    edges = []
    for n1 in G.nodes:
        for n2 in G.nodes:
            if int(n1) == int(n2-1):
                G.add_edge(n1, n2)
                edges.append((n1, n2))

    G.add_edge(len(boundary_coords)-1, 0)
    edges.append((len(boundary_coords)-1, 0))

                

    pos = nx.get_node_attributes(G, 'pos')
    node_color, edge_color = 'dodgerblue', 'dodgerblue' # 'gray' 'orange'

    nx.draw_networkx_nodes(G, pos, edge_color=edge_color, node_color=node_color, **kwargs)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_color)
    plt.show()
    plt.clf()

if __name__ == "__main__":
    check_visualisation()
