def DFS(graph, start):
    # Initialization
    stack = []
    color = {}
    T = {}
    d = {}
    f = {}
    for vertex in graph.keys():
        color[vertex] = 'b'
        T[vertex] = None
        d[vertex] = float('inf')
        f[vertex] = float('inf')
    t = 1
    color[start] = 'g'
    stack.append(start)
    d[start] = t
    
    # Main loop
    while stack:
        current_vertex = stack[-1]
        explored = True
        for adjacent_vertex in graph[current_vertex]:
            if color[adjacent_vertex] == 'b':
                color[adjacent_vertex] = 'g'
                stack.append(adjacent_vertex)
                T[adjacent_vertex] = current_vertex
                d[adjacent_vertex] = (t := t + 1)
                explored = False
                break
        if explored:
            stack.pop()
            color[current_vertex] = 'n'
            f[current_vertex] = (t := t + 1)
    
    # Print results
    print("Sommet\tParent\tD.O\tD.F")
    for vertex in graph.keys():
        print(f"{vertex}\t{T[vertex]}\t{d[vertex]}\t{f[vertex]}")
    return T, d, f

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
T, d, f = DFS(graph, start_vertex)