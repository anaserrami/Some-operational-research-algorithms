from collections import deque

def BFS_level_order(graph, start):
    # Initialization
    queue = deque()
    color = {}
    T = {}
    d = {}
    order = {}
    for vertex in graph.keys():
        color[vertex] = 'b'
        T[vertex] = None
        d[vertex] = len(graph)
    t = 0
    color[start] = 'g'
    queue.append(start)
    d[start] = 0
    order[start] = 1
    
    # Main loop
    while queue:
        current_vertex = queue.popleft()
        order[current_vertex] = t + 1
        t += 1
        color[current_vertex] = 'n'
        for adjacent_vertex in graph[current_vertex]:
            if color[adjacent_vertex] == 'b':
                color[adjacent_vertex] = 'g'
                T[adjacent_vertex] = current_vertex
                d[adjacent_vertex] = d[current_vertex] + 1
                queue.append(adjacent_vertex)
    
    # Print results
    print("Sommet\tParent\tNiveau\tOrder")
    for vertex in graph.keys():
        print(f"{vertex}\t{T[vertex]}\t{d[vertex]}\t{order[vertex]}")
    
    return T, d, order


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
T, d, order = BFS_level_order(graph, start_vertex)