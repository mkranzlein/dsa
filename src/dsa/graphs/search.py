from collections import defaultdict, deque


def beam_search():
    raise NotImplementedError


def bfs(adjacencies: defaultdict[set], root: int) -> list[int]:
    """Breadth-first search using a queue.

    Args:
        adjacencies: An adjacency list (as a dict of sets) describing a graph.
        root: The vertex ID where BFS should start.

    Returns:
        A list of nodes in the order they were visited during BFS.
    """
    queue = deque([root])
    visited = set([root])  # set for fast membership lookup
    visit_order = [root]  # list for ordered result of nodes visited

    while queue:
        v = queue.popleft()
        for neighbor in adjacencies[v]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                visit_order.append(neighbor)
    return visit_order


def dfs():
    raise NotImplementedError
