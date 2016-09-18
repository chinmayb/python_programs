graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

graph1 = {
    '0': ['1'],
    '1': ['3','2'],
    '2': ['4'],
    '3': ['0', '4'],
    '4': ['1']
}

def dfs_recursive(graph, start_node, visited=[]):
    """
    * Add to the visited array
    * Call the dfs method recursively, with the next non-visited node
      by looping through all the nodes connected to it.
    """
    if not visited:
        visited = []

    visited.append(start_node)

    for next_node in graph[start_node]:
        if next_node not in visited:
            print next_node
            dfs_recursive(graph, next_node, visited)

    return visited

def dfs_stack(graph, start_node):
    visited, stack = [], [start_node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex])
    return visited

#print dfs_recursive(graph1, '0')
#print dfs_stack(graph1, '0')

print dfs_recursive(graph, 'C')
print dfs_stack(graph, 'C')