def MST_Prim(G, r):
    S = set(G.keys()) # set of all vertices in the graph
    Q = S.copy() # set of vertices not yet added to the MST
    T = set() # set of vertices added to the MST
    Key = {v: float('inf') for v in S} # distance of each vertex from the MST
    Key[r] = 0 # distance of the root vertex is set to 0
    pi = {v: None for v in S} # parent of each vertex in the MST
    
    while Q:
        u = min(Q, key=lambda v: Key[v]) # extract the vertex with minimum Key value
        Q.remove(u) # remove u from Q
        T.add(u) # add u to T
        for v, w in G[u].items():
            if v in Q and w < Key[v]:
                pi[v] = u
                Key[v] = w
    
    return pi, Key

graph = {
    'V1': {'V2': 1, 'V3': 2, 'V5': 5, 'V6': 3, 'V7': 2},
    'V2': {'V1': 1, 'V3': 2},
    'V3': {'V1': 2, 'V2': 2, 'V4': 3, 'V7': 2},
    'V4': {'V3': 3, 'V5': 1, 'V7': 1},
    'V5': {'V1': 5, 'V4': 1, 'V6': 2, 'V7': 2},
    'V6': {'V1': 3, 'V5': 2},
    'V7': {'V1': 2, 'V3': 2, 'V4': 1, 'V5': 2}
}

start_vertex = 'V7'
pi, Key = MST_Prim(graph, start_vertex)
mst_weight = sum(Key.values())

def print_tree(current_vertex, parent_vertex, pi, indent=""):
    if current_vertex == parent_vertex:
        print(f"{current_vertex}")
    else:
        print(f"{indent}|__{current_vertex}")
    children = [v for v, p in pi.items() if p == current_vertex and v != parent_vertex]
    for child in children:
        print_tree(child, current_vertex, pi, indent + "   ")

print("Minimum Spanning Tree:")
print_tree(start_vertex, start_vertex, pi)

print(f"\nMinimum Spanning Tree weight: {mst_weight}")