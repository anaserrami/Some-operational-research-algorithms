def dijkstra_recursive(graph, node, visited, predecessors, distances):
    visited.add(node)

    if len(visited) == len(graph):
        return predecessors, distances

    for neighbor, weight in graph[node].items():
        if neighbor not in visited:
            distance_to_neighbor = distances[node] + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                predecessors[neighbor] = node

    unvisited_nodes = {node for node in distances if node not in visited}
    if not unvisited_nodes:
        return predecessors, distances

    next_node = min((distances[node], node) for node in unvisited_nodes)[1]
    return dijkstra_recursive(graph, next_node, visited, predecessors, distances)

graph = {
    'V1': {'V2': 10, 'V5': 5},
    'V2': {'V3': 1, 'V5': 2},
    'V3': {'V4': 4},
    'V4': {'V1': 7, 'V3': 6},
    'V5': {'V2': 3, 'V3': 9, 'V4': 2},
}
start_node = 'V1'
visited = set()
predecessors = {node: None for node in graph}
distances = {node: float('inf') for node in graph}
distances[start_node] = 0
predecessors[start_node] = None

predecessors, distances = dijkstra_recursive(graph, start_node, visited, predecessors, distances)

print("Shortest distances:")
for vertex, distance in distances.items():
    print(f"From {start_node} to {vertex}: {distance}")

print("\nPredecessors:")
for vertex, predecessor in predecessors.items():
    if predecessor is None:
        predecessor = 'None'
    print(f"{vertex}: {predecessor}")
