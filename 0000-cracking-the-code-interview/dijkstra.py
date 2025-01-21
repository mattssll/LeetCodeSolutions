# Mark the source node with a current distance of 0 and the rest with infinity.
# Set the non-visited node with the smallest current distance as the current node.
# For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1. If it is smaller than the current distance of Node, set it as the new current distance of N.
# Mark the current node 1 as visited.
# Go to step 2 if there are any nodes are unvisited.

graph = {
   "A": {"B": 3, "C": 2},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}
unvisited = set()
visited = set()
result_dict = {}
def dijkstra(graph, start):
    
    
    cur = start
    # 1. Mark the source node with a current distance of 0 and the rest with infinity.
    for k in graph.keys():
        for neighbour in graph[k]:
            if k==cur:
                result_dict[neighbour] = 0
                unvisited.add(neighbour)
            else:
                import math
                result_dict[neighbour] = math.inf
                unvisited.add(neighbour)

    # 2. Update distance of neighbours from start
    update_distance(node=start)
    

    print(result_dict)

def update_distance(node):
    for neighbour in graph[node]:
        # update values
        result_dict[neighbour] = graph[node][neighbour]
        # remove from visited
    unvisited.remove(node)
    print(f"removed {node} from unvisited")
    print("result set", result_dict)
    # pick smallest that is in unvisited
    min_element = min(unvisited, key=lambda x: result_dict[x])
    
    return update_distance(min_element)
 



dijkstra(graph, "A")
