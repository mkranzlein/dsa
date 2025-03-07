"""Implements breadth-first search with a queue."""

from collections import defaultdict, deque


def bfs(adjacencies: defaultdict[set], source: int):
    queue = deque([source])
    queue.append(source)

    visited_vertices = set()

    while queue:
        vertex = queue.popleft()
        print("Visited ", vertex)

        for neighboring_vertex in adjacencies[vertex]:
            if neighboring_vertex not in visited_vertices:
                queue.append(neighboring_vertex)
                visited_vertices.add(neighboring_vertex)

edges = [[1, 3],
         [2, 3],
         [4, 3],
         [5, 3]]

adjacencies = defaultdict(set)
for v_1, v_2 in edges:
    adjacencies[v_1].add(v_2)
    adjacencies[v_2].add(v_1)

print("Adjacencies")
for k, v in adjacencies.items():
    print(k, v)

