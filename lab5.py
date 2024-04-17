from collections import deque
def lazy_bfs(graph, start):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        yield vertex, path
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited and neighbor not in (v for v, _ in queue):
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("Ленивый BFS для графа:")
for vertex, path in lazy_bfs(graph, 'A'):
    print("Vertex:", vertex, "Path:", path)
