from collections import defaultdict


def postorder_dfs(root: int, adjacencies: dict[set[int]],
                  visited: set[int], result_stack: list[int]):
    """Postorder depth-first search.

    Root goes on stack after recursive call.
    Reversing postorder result (popping everything from stack) gives
    Topological ordering.

    Args:
        root: A root node ID.
        adjacencies: An adjacency list as a dict of sets.
        visited: The set of visited nodes.
        result_stack: A stack (list) of node IDs that have been visited.

    Returns:
        None. `visited` and `result_stack` are mutable and therfore updated
        during each call.
    """
    for neighbor in adjacencies[root]:
        if neighbor not in visited:
            visited.add(neighbor)
            postorder_dfs(neighbor, adjacencies, visited, result_stack)
    result_stack.append(root)
    return


def topo_sort(g: list[tuple[int]]):
    """Sorts a graph topologically.

    Assumes no cycles in graph. Uses DFS.

    Args:
        g: A graph expressed as a list of tuples, each representing a directed edge.
          For example, (6, 2) denotes an edge from vertex 6 to vertex 2.

    Returns:
        A sorted list of vertex IDs. Result not necessarily unique solution.
    """
    if len(g) == 0:
        return []

    # Source vertices appear as the first vertex of any edge
    # AND second vertex of NO edge
    sources, targets = zip(*g)
    sources, targets = set(sources), set(targets)
    sources = sources - targets

    adjacencies = defaultdict(set)
    for u, v in g:
        adjacencies[u].add(v)

    visited = set()
    result_stack = []

    while sources:
        root = sources.pop()  # Pick any unvisited source as root
        # Perform dfs. We don't need a return value from dfs
        # because unvisited_vertices and result_stack are mutable.
        postorder_dfs(root, adjacencies, visited, result_stack)

    return reversed(result_stack)
