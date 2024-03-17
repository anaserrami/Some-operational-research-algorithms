def Bellman_Ford_Moore(graph, start):
    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    
    # Relax edges repeatedly
    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
    
    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative-weight cycle")
                return None, None, False
    
    # Return distances and predecessors
    return predecessors, distances, True

graph = {
    'X1': {'X2': 6, 'X5': 7},
    'X2': {'X3': 5, 'X4': -4, 'X5': 8},
    'X3': {'X2': -2},
    'X4': {'X1': 2, 'X3': 7},
    'X5': {'X3': -3, 'X4': 9},
}

predecessors, distances, is_valid = Bellman_Ford_Moore(graph, 'X1')

if is_valid:
    # Print shortest distances
    print("Shortest distances:")
    for vertex in distances:
        print(f"From X1 to {vertex}: {distances[vertex]}")

    # Print predecessors
    print("\nPredecessors:")
    for vertex in predecessors:
        print(f"{vertex}: {predecessors[vertex]}")