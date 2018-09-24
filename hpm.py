import networkx as nx
import numpy as np
import random as rnd
import itertools


# @DONE Automated tuning of c for desired e_k.
# Caveat Emptor: This implementation doesn't worry too much about memory. random.random() is used,
# take necessary precautions if you want results to be reproducible.
def generate_network(N, e_k, omega=2.5):
    G = nx.empty_graph(N)

    # According to equation 4.29,  omega = (1 + 1/a)
    alpha = 1 / (omega - 1)

    # @TODO Can also solve the series sum analytically, approximation by definite integrals for example.
    # https://math.stackexchange.com/questions/1576502/calculate-finite-p-series

    # Series = SUM 1/n^(alpha) FOR n FROM 1 to N
    harmonic_series = np.power((1 / (np.arange(N) + 1)), alpha)
    c = (e_k * N) / np.sum(harmonic_series)

    # No need to recalculate the list of n, already have the harmonic series, just multiply by c, Eq. 4.28
    n_list = harmonic_series * c

    # n_expected is calculated to be e_k so it is unnecessary to recalculate it, to a very high precision.
    # unless you want to verify that e_k is correct.
    n_expected = e_k

    # Assign each node a hidden parameter n_i, they are generated above
    edges = itertools.combinations(range(N), 2)
    for e in edges:
        # compute probability of connecting two nodes based on equation under
        # Figure 4.18
        p = ((n_list[e[0]] * n_list[e[1]]) / (n_expected * N))
        if rnd.random() < p:
            G.add_edge(*e)

    return G
