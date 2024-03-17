import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    
    # Create a priority queue of vertices to visit
    queue = [(0, start)]
    
    # Visit vertices in the priority queue until it's empty
    visited = set()
    while queue:
        # Extract the vertex with the smallest distance from the queue
        current_distance, current_vertex = heapq.heappop(queue)
        visited.add(current_vertex)
        
        # Update distances and predecessors for neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue
            tentative_distance = current_distance + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(queue, (tentative_distance, neighbor))
    
    return predecessors, distances

graph = {
    'V1': {'V2': 10, 'V5': 5},
    'V2': {'V3': 1, 'V5': 2},
    'V3': {'V4': 4},
    'V4': {'V1': 7, 'V3': 6},
    'V5': {'V2': 3, 'V3': 9, 'V4': 2},
}

start_vertex = 'V1'
predecessors, distances = dijkstra(graph, start_vertex)

print("Shortest distances:")
for vertex, distance in distances.items():
    print(f"From {start_vertex} to {vertex}: {distance}")

print("\nPredecessors:")
for vertex, predecessor in predecessors.items():
    print(f"{vertex}: {predecessor}")