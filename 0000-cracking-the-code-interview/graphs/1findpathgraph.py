graph = {
    "a": ["b"],
    "b": ["c"],
    "d": ["e"]
}

# a to c, there is route
# a to e, no route

visited = set()
import collections
queue = collections.deque()
def bfs(node, end):
    if not node:
        return
    queue.append(node)
    while queue:
        node = queue.popleft()
        # c comes here, but if it has no Ns
        # then it wont go in for loop below
        if visit(node, end):
            return True
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append(neighbour)


def visit(node, end):
    print(node)
    visited.add(node)
    if node == end:
        print("true")
        return True

print(bfs("a", "b"))