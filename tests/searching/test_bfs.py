from collections import defaultdict

from searching.bfs import bfs


def test_bfs():
    edges = [[1, 3],
             [2, 3],
             [4, 3],
             [5, 3]]

    adjacencies = defaultdict(set)
    for u, v in edges:
        adjacencies[u].add(v)
        adjacencies[v].add(u)
    assert bfs(adjacencies, 1) == [1, 3, 2, 4, 5]
