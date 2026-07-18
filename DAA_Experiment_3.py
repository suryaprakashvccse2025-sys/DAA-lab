import time
import heapq

def prim(graph, n):
    visited = [False] * n
    min_heap = [(0, 0, -1)]

    mst = []
    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, weight))
            total_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_cost


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def kruskal(edges, n):
    ds = DisjointSet(n)

    mst = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_cost += w

    return mst, total_cost


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}
edges = []

print("Enter each edge (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

    edges.append((u, v, w))

start = time.perf_counter()

prim_mst, prim_cost = prim(graph, n)

end = time.perf_counter()

prim_time = (end - start) * 1000

start = time.perf_counter()

kruskal_mst, kruskal_cost = kruskal(edges, n)

end = time.perf_counter()

kruskal_time = (end - start) * 1000

print("\n========== PRIM'S MST ==========")

for u, v, w in prim_mst:
    print(f"Edge ({u} - {v})  Weight = {w}")

print("Total Cost :", prim_cost)
print("Edges Selected :", len(prim_mst))
print("Execution Time : {:.6f} ms".format(prim_time))

print("\n========== KRUSKAL'S MST ==========")

for u, v, w in kruskal_mst:
    print(f"Edge ({u} - {v})  Weight = {w}")

print("Total Cost :", kruskal_cost)
print("Edges Selected :", len(kruskal_mst))
print("Execution Time : {:.6f} ms".format(kruskal_time))

print("\n========== COMPARISON ==========")

print("{:<12}{:<15}{:<15}".format("Algorithm", "Total Cost", "Time(ms)"))
print("-" * 42)

print("{:<12}{:<15}{:<15.6f}".format(
    "Prim",
    prim_cost,
    prim_time
))

print("{:<12}{:<15}{:<15.6f}".format(
    "Kruskal",
    kruskal_cost,
    kruskal_time
))

if prim_cost == kruskal_cost:
    print("\nResult: Both algorithms produced the same Minimum Spanning Tree.")
else:
    print("\nResult: The algorithms produced different MST costs.")