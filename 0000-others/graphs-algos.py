# Iterative DFS with Stack - O(V+E)
from graphs import D

source = 0

seen = set()
seen.add(source)
stack = [source]  # visit first

while stack:
    node = stack.pop()  # process this one
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            stack.append(neighbour_node)
print("just printed via DFS, now via BFS\n")
# BFS (Queue) - O ( V + E )
source = 0
from collections import deque
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            q.append(neighbour_node)
