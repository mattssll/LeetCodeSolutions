# Array of Edges - directed [Start, End]
n = 8  # number of nodes
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]


def array_edges_to_adjacency_matrix():
    M = []
    for i in range(n):  # for N vertices we want N rows and N columns
        # Populate 8x8 matrix with all 0s
        M.append([0] * n)  # matrix multiplication

    for f, t in A:  # starting vertex U and ending vertex V
        M[f][t] = 1
        # if graph is undirected instead do
        # M[t][f] = 1  # diagonal matrix, strange thing...
    return M


def array_edges_to_adjacency_list():
    from collections import defaultdict

    D = defaultdict(list)  # makes default value for key being empty list

    for f, t in A:
        D[f].append(t)
    
    return D

print(f"Array of Edges:\n{A}")
M = array_edges_to_adjacency_matrix()
print(f"Adjacency Matrix\n{M}")
D = array_edges_to_adjacency_list()
print(f"Adjacency List\n{D}")
print(f"See neighbours of node 3 in Adj Matrix: {M[3]} - see neighbours of node 3 in adj list (cleaner) {D[3]}")