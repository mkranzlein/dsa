from collections import defaultdict


def get_adjacency_list(graph_edges: list[tuple[int, int]]) -> dict[set]:
    """Build an adjacency list from a graph described by its edges.

    Strictly speaking, the result is a dictionary of sets, not a list of lists.

    Args:
        graph_edges: A list of edges represented as tuples. For example, the
          tuple (5, 3) describes an edge from vertex 5 to vertex 3.

    Returns: An adjacency "list" represented as a dict where each key is a
      vertex and each value is a set containing adjacent vertices.
    """
    adjacencies = defaultdict(set)
    for u, v in graph_edges:
        adjacencies[u].add(v)
        adjacencies[v].add(u)
    return adjacencies
