def DFS(graph, start):
    # Initialization
    stack = []
    color = {}
    T = {}
    for vertex in graph.keys():
        color[vertex] = 'b'
        T[vertex] = None
    color[start] = 'g'
    stack.append(start)
    
    # Main loop
    while stack:
        current_vertex = stack[-1]
        found_unvisited_neighbor = False
        for adjacent_vertex in graph[current_vertex]:
            if color[adjacent_vertex] == 'b':
                found_unvisited_neighbor = True
                color[adjacent_vertex] = 'g'
                stack.append(adjacent_vertex)
                T[adjacent_vertex] = current_vertex
                break
        if not found_unvisited_neighbor:
            color[current_vertex] = 'n'
            stack.pop()
    
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
T = DFS(graph, start_vertex)