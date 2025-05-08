import heapq

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def prims_mst(graph):
    if not graph: return 0, []
    
    start = list(graph.keys())[0]
    pq = [(0, start, None)]
    visited = set()
    edges = []
    weight = 0
    
    while pq and len(visited) < len(graph):
        w, v, parent = heapq.heappop(pq)
        
        if v in visited: continue
        visited.add(v)
        
        if parent is not None:
            edges.append((parent, v, w))
            weight += w
            
        for neighbor, edge_w in graph[v]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_w, neighbor, v))
                
    return weight, edges

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
        
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
        
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return False
            
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskals_mst(graph):
    if not graph: return 0, []
    
    edges = [(w, u, v) for u in graph for v, w in graph[u] if u < v]
    edges.sort()
    
    vertices = list(graph.keys())
    ds = DisjointSet(vertices)
    
    mst = []
    total = 0
    
    for w, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == len(vertices) - 1:
                break
                
    return total, mst

def dijkstra(graph, start):
    distances = {v: float('infinity') for v in graph}
    distances[start] = 0
    pq = [(0, start)]
    paths = {}
    
    while pq:
        dist, vertex = heapq.heappop(pq)
        if dist > distances[vertex]: continue
            
        for neighbor, weight in graph[vertex]:
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                paths[neighbor] = vertex
                
    return distances, paths

def job_scheduling(jobs):
    if not jobs: return []
    
    jobs.sort(key=lambda x: x[2])
    selected = [jobs[0][0]]
    end_time = jobs[0][2]
    
    for job_id, start, end in jobs[1:]:
        if start >= end_time:
            selected.append(job_id)
            end_time = end
            
    return selected

def test_selection_sort():
    arr = [64, 25, 12, 22, 11]
    print("Selection Sort:")
    print(f"Original array: {arr}")
    print(f"Sorted array: {selection_sort(arr)}")
    print()

def test_prims_mst():
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    
    print("Prim's Minimum Spanning Tree:")
    total_weight, mst = prims_mst(graph)
    print(f"MST Edges: {mst}")
    print(f"Total Weight: {total_weight}")
    print()

def test_kruskals_mst():
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    
    print("Kruskal's Minimum Spanning Tree:")
    total_weight, mst = kruskals_mst(graph)
    print(f"MST Edges: {mst}")
    print(f"Total Weight: {total_weight}")
    print()

def test_dijkstra():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 5)],
        2: [(0, 1), (1, 2), (3, 8), (4, 10)],
        3: [(1, 5), (2, 8), (4, 2)],
        4: [(2, 10), (3, 2)]
    }
    
    print("Dijkstra's Shortest Path:")
    start_vertex = 0
    distances, paths = dijkstra(graph, start_vertex)
    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"  To vertex {vertex}: {distance}")
    print()

def test_job_scheduling():
    jobs = [(1, 1, 3), (2, 2, 5), (3, 4, 7), (4, 6, 9), (5, 5, 8)]
    
    print("Job Scheduling:")
    print(f"Selected jobs: {job_scheduling(jobs)}")
    print()

def main():
    test_selection_sort()
    test_prims_mst()
    test_kruskals_mst()
    test_dijkstra()
    test_job_scheduling()

main()