from graphs import graph
from searching.bfs import bfs


def test_bfs():
    edges = [[1, 3],
             [2, 3],
             [4, 3],
             [5, 3]]
    adjacencies = graph.get_adjacency_list(edges)
    assert bfs(adjacencies, 1) == [1, 3, 2, 4, 5]
