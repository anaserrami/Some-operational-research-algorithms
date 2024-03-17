from collections import deque

def BFS(graph, start):
    # Initialization
    queue = deque()
    color = {}
    T = {}
    for vertex in graph.keys():
        color[vertex] = 'b'
        T[vertex] = None
    color[start] = 'g'
    queue.append(start)
    
    # Main loop
    while queue:
        current_vertex = queue.popleft()
        color[current_vertex] = 'n'
        for adjacent_vertex in graph[current_vertex]:
            if color[adjacent_vertex] == 'b':
                color[adjacent_vertex] = 'g'
                T[adjacent_vertex] = current_vertex
                queue.append(adjacent_vertex)

    # Print results
    print("Sommet\tParent")
    for vertex in graph.keys():
        print(f"{vertex}\t{T[vertex]}")
    return T

graph = {
    'X1': ['X2', 'X3', 'X7', 'X8'],
    'X2': ['X1', 'X3', 'X5', 'X6', 'X8'],
    'X3': ['X1', 'X2', 'X4', 'X5'],
    'X4': ['X3', 'X5', 'X6'],
    'X5': ['X2', 'X3', 'X4', 'X6'],
    'X6': ['X2', 'X4', 'X5', 'X7', 'X8'],
    'X7': ['X1', 'X6', 'X8'],
    'X8': ['X1', 'X2', 'X6', 'X7']
}

start_vertex = 'X7'
T = BFS(graph, start_vertex)