def bellman_kalaba(graph, source):
    # Initialization
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Node traversal
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                # Update minimum distance
                if distances[neighbor] > distances[node] + graph[node][neighbor]:
                    distances[neighbor] = distances[node] + graph[node][neighbor]

    # Check for negative cycles
    for node in graph:
        for neighbor in graph[node]:
            if distances[neighbor] > distances[node] + graph[node][neighbor]:
                raise ValueError("The graph contains a negative cycle")

    return distances


graph = {
    'X1': {'X2': 6, 'X5': 7},
    'X2': {'X3': 5, 'X4': -4, 'X5': 8},
    'X3': {'X2': -2},
    'X4': {'X1': 2, 'X3': 7},
    'X5': {'X3': -3, 'X4': 9},
}

source_node = 'X1'
distances = bellman_kalaba(graph, source_node)

# Print the distances
for node, distance in distances.items():
    print(f"Shortest distance from {source_node} to {node}: {distance}")