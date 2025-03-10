from dsa.graphs import graph
from dsa.graphs import search


def test_bfs():
    edges = [[1, 3],
             [2, 3],
             [4, 3],
             [5, 3]]
    adjacencies = graph.get_adjacency_list(edges)
    assert search.bfs(adjacencies, 1) == [1, 3, 2, 4, 5]
