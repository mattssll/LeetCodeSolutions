from collections import defaultdict

graph = {
    "numpy": [],
    "pandas": ["numpy"],
    "matplotlib": ["numpy"],
    "scipy": ["numpy"],
    "seaborn": ["matplotlib", "numpy"],
}

def solve():
    indegree = defaultdict(int)

    # Step 1: Initialize indegree for all nodes
    for key in graph:
        indegree[key] = 0

    # Step 2: Compute indegree correctly
    for key in graph:
        for dep in graph[key]:
            indegree[key] += 1

    print("Indegree:", dict(indegree))

    # Step 3: Add nodes with indegree 0 to queue
    queue = [node for node in graph if indegree[node] == 0]

    print("Initial queue:", queue)
    result = []
    while queue:
        node = queue.pop()
        result.append(node)
        for pkg, dependencies in graph.items():
            if node in dependencies:
                indegree[pkg] -= 1
                if indegree[pkg] == 0:
                    queue.append(pkg)
    
    print("has no cycles") if len(result) == len(graph) else print("has cycle")
    return result

print(solve())