import networkx as nx
import numpy as np
import random as rnd
import itertools


def generate_network(N, e_k, omega=2.5, random_seed = 42):
    G = nx.empty_graph(N)

    # First generate the hidden parameters
    # For scale-free network, generate them using eq. 4.28

    # According to equation 4.29,  omega = (1 + 1/a)
    alpha = 1 / (omega - 1)
    # Expected degree of resulting network can be controlled by expected value of
    # hidden parameters n according to eq.s 4.27 and 4.28

    # @TODO Automated tuning of c for desired e_k.
    c = 114  # Constant c = 122.2 for N = 500 c = 684 for N = 5000, for a = 0.8
    n_list = [c / np.power(i, alpha) for i in np.arange(1, N + 1)]
    # Check if expected value is indeed what we are looking for.
    n_expected = sum(n_list) / N

    # Assign each node a hidden parameter n_i, they are generated above
    # Nodes are indexed from 0 - N-1 by Networkx, we can just have these indexes
    # be hidden parameter indexes and not bother with further assignments.
    edges = itertools.combinations(range(N), 2)
    for e in edges:
        # compute probability of connecting two nodes based on equation under
        # Figure 4.18
        p = ((n_list[e[0]] * n_list[e[1]]) / (n_expected * N))
        if rnd.random() < p:
            G.add_edge(*e)

    #degrees = G.degree()
    #sum_of_edges = sum(degrees.values())
    #print(sum_of_edges / N)

    return G