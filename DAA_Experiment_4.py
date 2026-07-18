import heapq
import time

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n
    visited = [False] * n

    dist[source] = 0
    pq = [(0, source)]

    visited_count = 0
    relaxations = 0

    while pq:
        current_dist, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        visited_count += 1

        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                relaxations += 1
                heapq.heappush(pq, (dist[v], v))

    return dist, prev, visited_count, relaxations


def print_path(prev, vertex):
    path = []

    while vertex != -1:
        path.append(vertex)
        vertex = prev[vertex]

    path.reverse()

    return " -> ".join(map(str, path))


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}

print("Enter each edge (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

source = int(input("Enter source vertex: "))

start = time.perf_counter()

dist, prev, visited, relax = dijkstra(graph, source)

end = time.perf_counter()

print("\n========== SHORTEST PATH ==========")

print("{:<10}{:<12}{}".format("Vertex", "Distance", "Path"))
print("-" * 40)

for i in range(n):
    if dist[i] == float('inf'):
        print("{:<10}{:<12}{}".format(i, "INF", "Not Reachable"))
    else:
        print("{:<10}{:<12}{}".format(i, dist[i], print_path(prev, i)))

print("\nVisited Nodes :", visited)
print("Edge Relaxations :", relax)
print("Execution Time : {:.6f} ms".format((end - start) * 1000))