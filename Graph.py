# """
# A graph is a collection of:
# Vertics (nodes) -> points
# Edges(links) -> connections between nodes


# Graph can be:
# Undirected / Directed
# Weighted / Unweighted
# Represented as :
# 1 Adjacency Matrix (2D array)
# 2 Adjancy List (dict or lists)

# """
# # Python Representation (Adjacency List)
# graph = {
#   "A": ["B", "C"],
#   "B": ["A", "D", "E"],
#   "C": ["A", "F"],
#   "D": ["B"],
#   "E": ["B", "F"],
#   "F": ["C", "E"]
    
# }

# # DFS Depth first Search  on Graph 
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start, end= " ")
#     for neightbour in graph[start]:
#         if neightbour not in visited:
#             dfs(graph, neightbour, visited)

# # BFS Breadth First search on graph 

# from collections import deque

# def bfs(graph, start):
#     visited =  set()
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node, end=" ")
#             visited.add(node)
#             queue.extend(graph[node])

# # Using Example
# print("DFS Traversal")
# dfs(graph, "A")

# print("\nBFS Traversal:")
# bfs(graph, "A")



# Graph using dictionary (Adjacency list)
graph = {
    "A": ["B"],
    "B": ["A","C"],
    "C": ["B"],
    "D": []
}

# Adding a new edges in this graph 
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)  # for undirected graph

add_edge(graph, "A", "C") # connected A and C
add_edge(graph, "A", "D")
print(graph)

from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start]) # queue starts with start node

    while queue:
        node = queue.popleft() # remove from front
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node]) # add all neightbours

# Run bfs from A
bfs(graph, "A")
